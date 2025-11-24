from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Event, Booking, Ticket, TicketType
from .forms import BookingForm
import uuid

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    
    def get_queryset(self):
        return Event.objects.filter(is_active=True).order_by('date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

class BookingCreateView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = BookingForm(event=event)
        return render(request, 'events/booking_form.html', {'event': event, 'form': form})

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = BookingForm(request.POST, event=event)
        
        if form.is_valid():
            # Calculate total amount and create booking
            total_amount = 0
            ticket_data = []
            
            for ticket_type in event.ticket_types.all():
                quantity = form.cleaned_data.get(f"ticket_{ticket_type.id}", 0)
                if quantity > 0:
                    total_amount += quantity * ticket_type.price
                    ticket_data.append({'type': ticket_type, 'quantity': quantity})
            
            booking = Booking.objects.create(
                customer_name=form.cleaned_data['customer_name'],
                customer_email=form.cleaned_data['customer_email'],
                customer_phone=form.cleaned_data['customer_phone'],
                total_amount=total_amount,
                payment_status='PENDING'
            )
            
            # Create tickets
            for item in ticket_data:
                for _ in range(item['quantity']):
                    Ticket.objects.create(
                        booking=booking,
                        ticket_type=item['type'],
                        ticket_code=str(uuid.uuid4())[:8].upper() # Simple 8-char code
                    )
            
            return redirect('events:booking_confirmation', booking_id=booking.id)
            
        return render(request, 'events/booking_form.html', {'event': event, 'form': form})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'events/booking_confirmation.html', {'booking': booking})
