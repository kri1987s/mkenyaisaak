from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Ticket, Booking

@require_http_methods(["GET"])
def verify_tickets_page(request):
    """
    Page where users can verify their tickets using various methods
    """
    return render(request, 'events/verify_tickets.html')

@require_http_methods(["GET", "POST"])
def verify_ticket_direct(request):
    """
    Page where users can enter their M-Pesa code to verify ticket
    """
    if request.method == 'POST':
        ticket_code = request.POST.get('ticket_code', '').strip().upper()

        if ticket_code:
            # First try to find by ticket code
            ticket = Ticket.objects.filter(ticket_code=ticket_code).select_related(
                'booking', 'ticket_type__event'
            ).first()

            if ticket:
                return render(request, 'events/ticket_verification_success.html', {
                    'ticket': ticket,
                    'booking': ticket.booking
                })

            # If ticket code not found, try to find by M-Pesa receipt number
            booking = Booking.objects.filter(
                mpesa_receipt_number__iexact=ticket_code
            ).select_related('tickets__ticket_type__event').first()

            if booking and booking.payment_status == 'PAID':
                return render(request, 'events/ticket_verification_success.html', {
                    'ticket': booking.tickets.first(),  # Show first ticket
                    'booking': booking
                })

            # If not found in DB, try to verify via M-Pesa API (in case callback was missed)
            from mpesa.utils import MpesaClient
            from .utils import check_mpesa_transaction_status

            # First, try treating the ticket_code as a CheckoutRequestID (original transaction ID)
            client = MpesaClient()
            mpesa_result = client.query_transaction_status(ticket_code)

            if 'error' not in mpesa_result:
                result_code = mpesa_result.get('ResponseCode')

                if result_code == '0':  # Transaction successful
                    # Extract the actual M-Pesa receipt number
                    result_params = mpesa_result.get('ResultParams', {})
                    if 'CallbackMetadata' in result_params:
                        items = result_params['CallbackMetadata'].get('Item', [])
                        mpesa_receipt_number = None
                        for item in items:
                            if item.get('Name') == 'MpesaReceiptNumber':
                                mpesa_receipt_number = item.get('Value')
                                break

                        # If the user entered the original CheckoutRequestID
                        checkout_request_id = mpesa_result.get('CheckoutRequestID')
                        if checkout_request_id == ticket_code:
                            # User entered the CheckoutRequestID
                            potential_booking = Booking.objects.filter(
                                payment_reference=checkout_request_id
                            ).first()

                            if potential_booking:
                                # Update the booking with the M-Pesa receipt number if not already set
                                if not potential_booking.mpesa_receipt_number:
                                    potential_booking.mpesa_receipt_number = mpesa_receipt_number
                                    potential_booking.payment_status = 'PAID'
                                    potential_booking.save()

                                return render(request, 'events/ticket_verification_success.html', {
                                    'ticket': potential_booking.tickets.first(),  # Show first ticket
                                    'booking': potential_booking
                                })
                        # If user entered the M-Pesa receipt number, try to find booking by receipt number in DB
                        elif mpesa_receipt_number == ticket_code:
                            # User entered the M-Pesa receipt number
                            # Find the booking associated with this receipt number in DB
                            # The booking might exist but have been missed in the original search
                            booking_by_receipt = Booking.objects.filter(
                                mpesa_receipt_number__iexact=ticket_code
                            ).select_related('tickets__ticket_type__event').first()

                            if booking_by_receipt and booking_by_receipt.payment_status == 'PAID':
                                return render(request, 'events/ticket_verification_success.html', {
                                    'ticket': booking_by_receipt.tickets.first(),  # Show first ticket
                                    'booking': booking_by_receipt
                                })

            # If that didn't work, maybe the ticket_code is an M-Pesa receipt number that exists in our DB
            # This is a fallback in case the receipt was already saved but search was case-sensitive
            booking_fallback = Booking.objects.filter(
                mpesa_receipt_number__iexact=ticket_code
            ).select_related('tickets__ticket_type__event').first()

            if booking_fallback and booking_fallback.payment_status == 'PAID':
                return render(request, 'events/ticket_verification_success.html', {
                    'ticket': booking_fallback.tickets.first(),  # Show first ticket
                    'booking': booking_fallback
                })

            # If still not found, show error
            return render(request, 'events/ticket_verification.html', {
                'error_message': 'Ticket not found. Please check your M-Pesa code and try again.',
                'ticket_code': ticket_code
            })

        else:
            return render(request, 'events/ticket_verification.html', {
                'error_message': 'Please enter a ticket code or M-Pesa receipt number.'
            })

    # GET request - show the verification form
    return render(request, 'events/ticket_verification.html')

def verify_ticket_from_event(request, event_id):
    """
    Verify ticket from event detail page - handles AJAX request
    """
    from django.http import JsonResponse
    from .models import Event
    import json

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ticket_code = data.get('ticket_code', '').strip().upper()

            if not ticket_code:
                return JsonResponse({'status': 'error', 'message': 'Ticket code is required'})

            event = get_object_or_404(Event, id=event_id)

            # First try to find by ticket code
            ticket = Ticket.objects.filter(
                ticket_code=ticket_code,
                ticket_type__event=event
            ).select_related('booking', 'ticket_type__event').first()

            if ticket:
                return JsonResponse({
                    'status': 'success',
                    'ticket': {
                        'ticket_code': ticket.ticket_code,
                        'customer_name': ticket.booking.customer_name,
                        'customer_phone': ticket.booking.customer_phone,
                        'ticket_type': ticket.ticket_type.name,
                        'payment_status': ticket.booking.payment_status,
                        'mpesa_receipt': ticket.booking.mpesa_receipt_number,
                        'event_title': ticket.ticket_type.event.title
                    }
                })

            # If ticket code not found, try to find by M-Pesa receipt number
            booking = Booking.objects.filter(
                mpesa_receipt_number__iexact=ticket_code,
                tickets__ticket_type__event=event
            ).select_related('tickets__ticket_type__event').first()

            if booking and booking.payment_status == 'PAID':
                return JsonResponse({
                    'status': 'success',
                    'ticket': {
                        'ticket_code': booking.tickets.first().ticket_code if booking.tickets.first() else 'N/A',
                        'customer_name': booking.customer_name,
                        'customer_phone': booking.customer_phone,
                        'ticket_type': booking.tickets.first().ticket_type.name if booking.tickets.first() else 'N/A',
                        'payment_status': booking.payment_status,
                        'mpesa_receipt': booking.mpesa_receipt_number,
                        'event_title': booking.tickets.first().ticket_type.event.title if booking.tickets.first() else 'N/A'
                    }
                })

            # If not found in DB, try to verify via M-Pesa API (in case callback was missed)
            from mpesa.utils import MpesaClient
            from .utils import check_mpesa_transaction_status

            # First, try treating the ticket_code as a CheckoutRequestID (original transaction ID)
            client = MpesaClient()
            mpesa_result = client.query_transaction_status(ticket_code)

            if 'error' not in mpesa_result:
                result_code = mpesa_result.get('ResponseCode')

                if result_code == '0':  # Transaction successful
                    # Extract the actual M-Pesa receipt number
                    result_params = mpesa_result.get('ResultParams', {})
                    if 'CallbackMetadata' in result_params:
                        items = result_params['CallbackMetadata'].get('Item', [])
                        mpesa_receipt_number = None
                        for item in items:
                            if item.get('Name') == 'MpesaReceiptNumber':
                                mpesa_receipt_number = item.get('Value')
                                break

                        # If the user entered the original CheckoutRequestID
                        checkout_request_id = mpesa_result.get('CheckoutRequestID')
                        if checkout_request_id == ticket_code:
                            # User entered the CheckoutRequestID
                            potential_booking = Booking.objects.filter(
                                payment_reference=checkout_request_id,
                                tickets__ticket_type__event=event
                            ).select_related('tickets__ticket_type__event').first()

                            if potential_booking:
                                # Update the booking with the M-Pesa receipt number if not already set
                                if not potential_booking.mpesa_receipt_number:
                                    potential_booking.mpesa_receipt_number = mpesa_receipt_number
                                    potential_booking.payment_status = 'PAID'
                                    potential_booking.save()

                                return JsonResponse({
                                    'status': 'success',
                                    'ticket': {
                                        'ticket_code': potential_booking.tickets.first().ticket_code if potential_booking.tickets.first() else 'N/A',
                                        'customer_name': potential_booking.customer_name,
                                        'customer_phone': potential_booking.customer_phone,
                                        'ticket_type': potential_booking.tickets.first().ticket_type.name if potential_booking.tickets.first() else 'N/A',
                                        'payment_status': potential_booking.payment_status,
                                        'mpesa_receipt': potential_booking.mpesa_receipt_number,
                                        'event_title': potential_booking.tickets.first().ticket_type.event.title if potential_booking.tickets.first() else 'N/A'
                                    }
                                })
                        # If user entered the M-Pesa receipt number
                        elif mpesa_receipt_number == ticket_code:
                            # User entered the M-Pesa receipt number
                            booking_by_receipt = Booking.objects.filter(
                                mpesa_receipt_number__iexact=ticket_code,
                                tickets__ticket_type__event=event
                            ).select_related('tickets__ticket_type__event').first()

                            if booking_by_receipt and booking_by_receipt.payment_status == 'PAID':
                                return JsonResponse({
                                    'status': 'success',
                                    'ticket': {
                                        'ticket_code': booking_by_receipt.tickets.first().ticket_code if booking_by_receipt.tickets.first() else 'N/A',
                                        'customer_name': booking_by_receipt.customer_name,
                                        'customer_phone': booking_by_receipt.customer_phone,
                                        'ticket_type': booking_by_receipt.tickets.first().ticket_type.name if booking_by_receipt.tickets.first() else 'N/A',
                                        'payment_status': booking_by_receipt.payment_status,
                                        'mpesa_receipt': booking_by_receipt.mpesa_receipt_number,
                                        'event_title': booking_by_receipt.tickets.first().ticket_type.event.title if booking_by_receipt.tickets.first() else 'N/A'
                                    }
                                })

            # If that didn't work, maybe the ticket_code is an M-Pesa receipt number that exists in our DB
            booking_fallback = Booking.objects.filter(
                mpesa_receipt_number__iexact=ticket_code,
                tickets__ticket_type__event=event
            ).select_related('tickets__ticket_type__event').first()

            if booking_fallback and booking_fallback.payment_status == 'PAID':
                return JsonResponse({
                    'status': 'success',
                    'ticket': {
                        'ticket_code': booking_fallback.tickets.first().ticket_code if booking_fallback.tickets.first() else 'N/A',
                        'customer_name': booking_fallback.customer_name,
                        'customer_phone': booking_fallback.customer_phone,
                        'ticket_type': booking_fallback.tickets.first().ticket_type.name if booking_fallback.tickets.first() else 'N/A',
                        'payment_status': booking_fallback.payment_status,
                        'mpesa_receipt': booking_fallback.mpesa_receipt_number,
                        'event_title': booking_fallback.tickets.first().ticket_type.event.title if booking_fallback.tickets.first() else 'N/A'
                    }
                })

            # If still not found
            return JsonResponse({'status': 'error', 'message': 'Ticket not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})