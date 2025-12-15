from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Event, Booking, Ticket, TicketType
from .forms import BookingForm, PerformanceForm
from mpesa.utils import MpesaClient
from .utils import send_ticket_confirmation_email
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_url'] = self.request.build_absolute_uri()
        return context

class BookingCreateView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = BookingForm(event=event)
        context = {
            'event': event,
            'form': form,
            'current_url': request.build_absolute_uri(),
        }
        return render(request, 'events/booking_form.html', context)

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

            if total_amount == 0:
                messages.error(request, "Please select at least one ticket.")
                return render(request, 'events/booking_form.html', {'event': event, 'form': form})

            phone_number = form.cleaned_data['customer_phone']
            # Format phone number for M-Pesa (254...)
            if phone_number.startswith('0'):
                mpesa_phone = '254' + phone_number[1:]
            elif phone_number.startswith('+254'):
                mpesa_phone = phone_number[1:]
            else:
                mpesa_phone = phone_number

            booking = Booking.objects.create(
                customer_name=form.cleaned_data['customer_name'],
                customer_email=form.cleaned_data['customer_email'],
                customer_phone=phone_number,
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

            # Initiate M-Pesa STK Push
            client = MpesaClient()
            callback_url = request.build_absolute_uri('/mpesa/callback/')
            account_reference = f"BK-{booking.id}"[:12] # Shorten if needed
            transaction_desc = f"Tickets for {event.title}"[:13]

            try:
                response = client.make_stk_push(
                    phone_number=mpesa_phone,
                    amount=int(total_amount), # M-Pesa expects integer for amount usually, or check API
                    account_reference=account_reference,
                    transaction_desc=transaction_desc,
                    callback_url=callback_url
                )

                if response and 'ResponseCode' in response and response['ResponseCode'] == '0':
                    # Success
                    checkout_request_id = response.get('CheckoutRequestID')
                    booking.payment_reference = checkout_request_id
                    booking.save()
                    messages.success(request, f"STK Push sent to {phone_number}. Please complete payment.")
                    return redirect('events:ticket_view', booking_id=booking.id)
                else:
                    error_msg = response.get('errorMessage', 'Unknown error') if response else 'Connection failed'
                    booking.delete()  # Delete the booking if M-Pesa failed
                    messages.error(request, f"M-Pesa Error: {error_msg}")
                    return render(request, 'events/booking_form.html', {'event': event, 'form': form})

            except Exception as e:
                booking.delete()  # Delete the booking if system error occurred
                messages.error(request, f"System Error: {str(e)}")
                return render(request, 'events/booking_form.html', {'event': event, 'form': form})

        return render(request, 'events/booking_form.html', {'event': event, 'form': form})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    context = {
        'booking': booking,
        'current_url': request.build_absolute_uri(),
    }
    return render(request, 'events/booking_confirmation.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def send_receipt_email(request, booking_id):
    """Send receipt to email for a specific booking"""
    booking = get_object_or_404(Booking, id=booking_id)

    import json
    data = json.loads(request.body)
    email = data.get('email', '').strip()

    if not email:
        return JsonResponse({'success': False, 'message': 'Email is required'})

    # Update booking with the email provided in the form
    original_email = booking.customer_email  # Store original email for comparison
    booking.customer_email = email
    booking.save()

    try:
        # Send the ticket confirmation email
        send_ticket_confirmation_email(booking)
        return JsonResponse({'success': True, 'message': f'Receipt sent successfully to {email}!'})
    except Exception as e:
        # Log the error for debugging
        import logging
        logging.exception(f"Failed to send email receipt to {email} for booking {booking_id}")
        return JsonResponse({'success': False, 'message': f'Failed to send email: {str(e)}'})


def performance_registration(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    performances = event.performances.all().order_by('name')

    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            performance = form.save(commit=False)
            performance.event = event
            performance.save()
            messages.success(request, 'Performance registration submitted successfully!')
            return redirect('events:performance_registration', event_id=event.id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PerformanceForm(initial={'event': event})

    # Get unique phone numbers
    phone_numbers = performances.values_list('phone_number', flat=True)
    unique_phone_numbers = sorted(list(set(phone_numbers)))

    context = {
        'event': event,
        'form': form,
        'performances': performances,
        'unique_phone_numbers': unique_phone_numbers,
        'current_url': request.build_absolute_uri(),
    }
    return render(request, 'events/performance_registration.html', context)
