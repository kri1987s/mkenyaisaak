from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Ticket, Booking

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
            
            # If not found, show error
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

            # If not found
            return JsonResponse({'status': 'error', 'message': 'Ticket not found'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})