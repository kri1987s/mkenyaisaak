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

        # Check status for all pending bookings by querying M-Pesa
        for booking in bookings:
            if booking.payment_status == 'PENDING' and booking.payment_reference:
                # Check if this pending booking has been paid by querying M-Pesa
                from .utils import check_mpesa_transaction_status
                check_mpesa_transaction_status(booking)
                # Refresh from DB to get any updates
                booking.refresh_from_db()

        # Group all bookings by event for better organization
        from collections import defaultdict
        bookings_by_event = defaultdict(list)

        for booking in bookings:
            # Get the event from the first associated ticket
            first_ticket = booking.tickets.first()
            event_name = "Unknown Event"
            if first_ticket and first_ticket.ticket_type.event:
                event_name = first_ticket.ticket_type.event.title

            # Collect detailed ticket information
            ticket_details = []
            ticket_types = set()
            total_admissions = 0

            for ticket in booking.tickets.all():
                ticket_details.append({
                    'ticket_code': ticket.ticket_code,
                    'ticket_type': ticket.ticket_type.name if ticket.ticket_type else 'Unknown',
                    'admissions': 1  # Each ticket admits 1 person unless it's a family ticket
                })
                ticket_types.add(ticket.ticket_type.name if ticket.ticket_type else 'Unknown')
                # For family tickets, adjust admissions count
                if ticket.ticket_type and 'family' in ticket.ticket_type.name.lower():
                    total_admissions += 4  # Family ticket admits 4 people
                else:
                    total_admissions += 1  # Regular ticket admits 1 person

            booking_info = {
                'booking_id': str(booking.id),
                'customer_name': booking.customer_name,
                'payment_status': booking.payment_status,
                'payment_reference': booking.payment_reference,
                'mpesa_receipt_number': booking.mpesa_receipt_number,
                'total_amount': str(booking.total_amount),
                'created_at': booking.created_at.isoformat(),
                'updated_at': booking.updated_at.isoformat(),
                'ticket_count': booking.tickets.count(),
                'ticket_codes': [ticket.ticket_code for ticket in booking.tickets.all()],
                'ticket_types': list(ticket_types),
                'ticket_details': ticket_details,
                'admissions': total_admissions
            }

            bookings_by_event[event_name].append(booking_info)

        # Return all bookings grouped by event
        all_bookings_grouped = {}
        for event_name, booking_list in bookings_by_event.items():
            all_bookings_grouped[event_name] = sorted(booking_list, key=lambda x: x['created_at'], reverse=True)

        return JsonResponse({
            'status': 'success',
            'booking_groups': all_bookings_grouped,
            'total_bookings': len(bookings),
            'phone_number': formatted_phone
        })

    # If no bookings found for this phone number
    return JsonResponse({
        'status': 'success',  // Return success but with empty groups
        'booking_groups': {},
        'total_bookings': 0,
        'phone_number': formatted_phone
    })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)