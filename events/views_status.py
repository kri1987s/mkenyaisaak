from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import Booking
from .utils import check_mpesa_transaction_status


@require_http_methods(["GET"])
def check_payment_status(request, booking_id):
    """
    API endpoint to check payment status by booking ID
    Also tries to fetch M-Pesa receipt if not yet available
    """
    try:
        booking = get_object_or_404(Booking, id=booking_id)

        # If we don't have an M-Pesa receipt number yet and the status is PAID,
        # try to fetch it from M-Pesa API
        if not booking.mpesa_receipt_number and booking.payment_status == 'PAID':
            check_mpesa_transaction_status(booking)
            # Refresh the booking instance to get the updated data
            booking.refresh_from_db()

        return JsonResponse({
            'status': 'success',
            'payment_status': booking.payment_status,
            'payment_reference': booking.payment_reference,
            'mpesa_receipt_number': booking.mpesa_receipt_number,
            'total_amount': str(booking.total_amount),
            'updated_at': booking.updated_at.isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@require_http_methods(["GET"])
def check_payment_status_by_reference(request):
    """
    API endpoint to check payment status by payment reference (CheckoutRequestID)
    Useful for when users only have the original reference ID
    Also tries to fetch M-Pesa receipt if not yet available
    """
    payment_reference = request.GET.get('ref', None)

    if not payment_reference:
        return JsonResponse({
            'status': 'error',
            'message': 'Payment reference is required'
        }, status=400)

    try:
        booking = get_object_or_404(Booking, payment_reference=payment_reference)

        # If we don't have an M-Pesa receipt number yet and the status is PAID,
        # try to fetch it from M-Pesa API
        if not booking.mpesa_receipt_number and booking.payment_status == 'PAID':
            check_mpesa_transaction_status(booking)
            # Refresh the booking instance to get the updated data
            booking.refresh_from_db()

        return JsonResponse({
            'status': 'success',
            'booking_id': str(booking.id),
            'payment_status': booking.payment_status,
            'payment_reference': booking.payment_reference,
            'mpesa_receipt_number': booking.mpesa_receipt_number,
            'total_amount': str(booking.total_amount),
            'updated_at': booking.updated_at.isoformat()
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@require_http_methods(["GET"])
def check_payment_status_by_receipt(request):
    """
    API endpoint to check payment status by M-Pesa receipt number
    Useful for when users only have the M-Pesa receipt number (retrieved from their SMS)
    """
    mpesa_receipt_number = request.GET.get('receipt', None)

    if not mpesa_receipt_number:
        return JsonResponse({
            'status': 'error',
            'message': 'M-Pesa receipt number is required'
        }, status=400)

    try:
        # Find booking by M-Pesa receipt number (case-insensitive)
        booking = Booking.objects.get(mpesa_receipt_number__iexact=mpesa_receipt_number)

        return JsonResponse({
            'status': 'success',
            'booking_id': str(booking.id),
            'payment_status': booking.payment_status,
            'payment_reference': booking.payment_reference,
            'mpesa_receipt_number': booking.mpesa_receipt_number,
            'total_amount': str(booking.total_amount),
            'updated_at': booking.updated_at.isoformat()
        })
    except Booking.DoesNotExist:
        # If not found in DB, return appropriate error
        return JsonResponse({
            'status': 'error',
            'message': 'Booking with this M-Pesa receipt number not found. Please check the receipt number and try again.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@require_http_methods(["GET"])
def check_payment_status_by_phone(request):
    """
    API endpoint to check payment status by customer phone number
    This handles the scenario where user paid but callback was lost,
    so we need to query M-Pesa directly using their phone number
    """
    phone_number = request.GET.get('phone', None)

    if not phone_number:
        return JsonResponse({
            'status': 'error',
            'message': 'Phone number is required'
        }, status=400)

    try:
        # Format phone number consistently (to 254 format)
        if phone_number.startswith('0'):
            formatted_phone = '254' + phone_number[1:]
        elif phone_number.startswith('+254'):
            formatted_phone = phone_number[1:]
        else:
            formatted_phone = phone_number

        # Find all bookings with this phone number (could be multiple)
        bookings = Booking.objects.filter(customer_phone__endswith=formatted_phone[-9:]).order_by('-created_at')  # Last 9 digits should match

        # First, separate PAID and PENDING bookings
        paid_bookings = []
        pending_bookings = []

        for booking in bookings:
            if booking.payment_status == 'PAID':
                paid_bookings.append(booking)
            elif booking.payment_status == 'PENDING' and booking.payment_reference:
                # Check if this pending booking has been paid by querying M-Pesa
                from .utils import check_mpesa_transaction_status
                check_mpesa_transaction_status(booking)
                # Refresh from DB to get any updates
                booking.refresh_from_db()

                if booking.payment_status == 'PAID':
                    paid_bookings.append(booking)
                else:
                    pending_bookings.append(booking)

        # If we have any paid bookings, prioritize showing those
        if paid_bookings:
            # Return the most recent paid booking
            latest_paid = paid_bookings[0]  # They're already ordered by -created_at

            # Prepare list of all paid bookings
            all_paid_bookings = []
            for booking in paid_bookings:
                all_paid_bookings.append({
                    'booking_id': str(booking.id),
                    'payment_status': booking.payment_status,
                    'payment_reference': booking.payment_reference,
                    'mpesa_receipt_number': booking.mpesa_receipt_number,
                    'total_amount': str(booking.total_amount),
                    'created_at': booking.created_at.isoformat()
                })

            return JsonResponse({
                'status': 'success',
                'booking_id': str(latest_paid.id),
                'payment_status': latest_paid.payment_status,
                'payment_reference': latest_paid.payment_reference,
                'mpesa_receipt_number': latest_paid.mpesa_receipt_number,
                'total_amount': str(latest_paid.total_amount),
                'updated_at': latest_paid.updated_at.isoformat(),
                'all_paid_bookings': all_paid_bookings  # Include all paid bookings from this phone
            })

        # If no paid bookings, show pending ones (with most recent first)
        if pending_bookings:
            latest_pending = pending_bookings[0]  # Most recent

            all_pending_info = []
            for booking in pending_bookings:
                all_pending_info.append({
                    'booking_id': str(booking.id),
                    'payment_status': booking.payment_status,
                    'payment_reference': booking.payment_reference,
                    'mpesa_receipt_number': booking.mpesa_receipt_number,
                    'total_amount': str(booking.total_amount),
                    'created_at': booking.created_at.isoformat()
                })

            return JsonResponse({
                'status': 'partial_success',
                'booking_id': str(latest_pending.id),
                'payment_status': latest_pending.payment_status,
                'payment_reference': latest_pending.payment_reference,
                'mpesa_receipt_number': latest_pending.mpesa_receipt_number,
                'total_amount': str(latest_pending.total_amount),
                'updated_at': latest_pending.updated_at.isoformat(),
                'all_pending_bookings': all_pending_info
            })

        # If no bookings found for this phone number
        return JsonResponse({
            'status': 'error',
            'message': 'No booking found for this phone number. Please make sure you used this number when booking.'
        }, status=404)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)