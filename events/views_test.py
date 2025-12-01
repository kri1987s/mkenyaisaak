from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib import messages
from .models import Event, Booking, Ticket
from .forms import BookingForm
from mpesa.utils import MpesaClient
import uuid

class TestBookingCreateView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = BookingForm(event=event)
        return render(request, 'events/booking_form_test.html', {'event': event, 'form': form})

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
                return render(request, 'events/booking_form_test.html', {'event': event, 'form': form})

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
                        ticket_code=str(uuid.uuid4())[:8].upper()
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
                else:
                    error_msg = response.get('errorMessage', 'Unknown error') if response else 'Connection failed'
                    messages.error(request, f"M-Pesa Error: {error_msg}")
                    
            except Exception as e:
                messages.error(request, f"System Error: {str(e)}")

            return redirect('events:test_ticket', booking_id=booking.id)
            
        return render(request, 'events/booking_form_test.html', {'event': event, 'form': form})

def test_ticket_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'events/ticket_test.html', {'booking': booking})
