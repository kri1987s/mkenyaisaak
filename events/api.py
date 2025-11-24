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
        
        ticket = Ticket.objects.filter(ticket_code=ticket_code).select_related('booking', 'ticket_type__event').first()
        
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
