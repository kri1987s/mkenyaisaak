from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.utils import timezone
import json
from .models import Event, Ticket

@staff_member_required
@require_http_methods(["GET"])
def get_event_attendees(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = Ticket.objects.filter(ticket_type__event=event).select_related('booking', 'ticket_type')
    
    data = []
    for ticket in tickets:
        data.append({
            'id': ticket.id,
            'ticket_code': ticket.ticket_code,
            'customer_name': ticket.booking.customer_name,
            'customer_phone': ticket.booking.customer_phone,
            'ticket_type': ticket.ticket_type.name,
            'payment_status': ticket.booking.payment_status,
            'gate1': bool(ticket.checked_in_at_gate1),
            'gate2': bool(ticket.checked_in_at_gate2),
        })
    
    return JsonResponse(data, safe=False)

@csrf_exempt
@staff_member_required
@require_http_methods(["POST"])
def update_ticket_status(request):
    try:
        data = json.loads(request.body)
        ticket_id = data.get('id')
        field = data.get('field') # 'gate1' or 'gate2'
        value = data.get('value') # boolean
        
        ticket = Ticket.objects.get(pk=ticket_id)
        
        ticket.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@staff_member_required
@require_http_methods(["POST"])
def verify_ticket(request, gate_number):
    try:
        data = json.loads(request.body)
        ticket_code = data.get('ticket_code')

        # First try to find by ticket code
        ticket = Ticket.objects.filter(ticket_code=ticket_code).select_related('booking', 'ticket_type__event').first()

        if not ticket:
            # If ticket code not found, try to find by M-Pesa receipt number
            from .models import Booking
            booking = Booking.objects.filter(
                mpesa_receipt_number__iexact=ticket_code
            ).select_related('tickets__ticket_type__event').first()

            if booking and booking.payment_status == 'PAID':
                ticket = booking.tickets.first()
            else:
                # If not found in DB, try to verify via M-Pesa API (in case callback was missed)
                from mpesa.utils import MpesaClient
                from .utils import check_mpesa_transaction_status

                # Try to query M-Pesa directly with the ticket_code to see if it's a valid M-Pesa receipt
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

                            # If the user entered the M-Pesa receipt number directly
                            if mpesa_receipt_number == ticket_code:
                                # User entered the actual M-Pesa receipt number
                                checkout_request_id = mpesa_result.get('CheckoutRequestID')
                                if checkout_request_id:
                                    potential_booking = Booking.objects.filter(
                                        payment_reference=checkout_request_id
                                    ).first()

                                    if potential_booking:
                                        # Update the booking with the M-Pesa receipt number if not already set
                                        if not potential_booking.mpesa_receipt_number:
                                            potential_booking.mpesa_receipt_number = mpesa_receipt_number
                                            potential_booking.payment_status = 'PAID'
                                            potential_booking.save()

                                        ticket = potential_booking.tickets.first()

        if not ticket:
            return JsonResponse({'status': 'error', 'message': 'Invalid Ticket Code'}, status=404)

        # Check if event is active
        if not ticket.ticket_type.event.is_active:
             return JsonResponse({'status': 'error', 'message': 'Event is not active'}, status=400)

        attendee_name = ticket.booking.customer_name
        ticket_type = ticket.ticket_type.name

        if gate_number == 'gate1':
            if ticket.checked_in_at_gate1:
                return JsonResponse({
                    'status': 'warning',
                    'message': f'ALREADY CHECKED IN (Gate 1) at {ticket.checked_in_at_gate1.strftime("%H:%M")}',
                    'attendee': attendee_name,
                    'type': ticket_type
                })
            ticket.checked_in_at_gate1 = timezone.now()

        elif gate_number == 'gate2':
            if not ticket.checked_in_at_gate1:
                 return JsonResponse({
                    'status': 'error',
                    'message': 'NOT CHECKED IN AT GATE 1',
                    'attendee': attendee_name,
                    'type': ticket_type
                })

            if ticket.checked_in_at_gate2:
                return JsonResponse({
                    'status': 'warning',
                    'message': f'ALREADY CHECKED IN (Gate 2) at {ticket.checked_in_at_gate2.strftime("%H:%M")}',
                    'attendee': attendee_name,
                    'type': ticket_type
                })
            ticket.checked_in_at_gate2 = timezone.now()

        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid Gate'}, status=400)

        ticket.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Check-in Successful',
            'attendee': attendee_name,
            'type': ticket_type
        })

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
