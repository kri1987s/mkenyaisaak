import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name=f"qr_{data}.png")

def send_ticket_confirmation_email(booking):
    subject = f"Your Tickets for {booking.tickets.first().ticket_type.event.title}"

    # Generate QR codes for all tickets if not already generated
    for ticket in booking.tickets.all():
        if not ticket.qr_code:
            ticket.qr_code = generate_qr_code(ticket.ticket_code)
            ticket.save()

    html_message = render_to_string('events/emails/ticket_confirmation.html', {'booking': booking})
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [booking.customer_email],
        html_message=html_message,
        fail_silently=False,
    )


def send_booking_notification_email(booking):
    """Send booking notification email to the event organizer"""
    # Get the event associated with this booking
    event = booking.tickets.first().ticket_type.event if booking.tickets.first() else None

    if not event or not event.notification_email:
        # If no notification email is set, exit early
        return

    subject = f"New Booking Notification - {event.title}"

    context = {
        'booking': booking,
        'event': event,
    }

    html_message = render_to_string('events/emails/booking_notification.html', context)
    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@mkenyaisaak.com',
        recipient_list=[event.notification_email],
        html_message=html_message,
        fail_silently=False,
    )


def check_mpesa_transaction_status(booking):
    """
    Check the status of an M-Pesa transaction and update the booking if needed
    """
    from mpesa.utils import MpesaClient
    from django.utils import timezone

    # Only check if we have a payment reference and no M-Pesa receipt number yet
    if not booking.payment_reference or booking.mpesa_receipt_number:
        return False

    client = MpesaClient()
    result = client.query_transaction_status(booking.payment_reference)

    print(f"M-Pesa Query Result for {booking.payment_reference}: {result}")

    if 'error' in result:
        print(f"Error querying transaction status: {result['error']}")
        return False

    # Process the response to extract M-Pesa receipt number
    response_code = result.get('ResponseCode')

    if response_code == '0':
        # Transaction has been completed successfully
        # Extract M-Pesa receipt number from the response
        result_params = result.get('ResultParams', {})
        if 'TransactionID' in result_params:
            mpesa_receipt_number = result_params['TransactionID']
            booking.mpesa_receipt_number = mpesa_receipt_number
            booking.payment_status = 'PAID'  # Ensure status is PAID
            booking.save()
            print(f"Updated booking {booking.id} with M-Pesa receipt: {mpesa_receipt_number}")
            return True
        elif 'CallbackMetadata' in result_params:
            # Try to get from CallbackMetadata
            callback_metadata = result_params['CallbackMetadata']
            items = callback_metadata.get('Item', [])
            for item in items:
                if item.get('Name') == 'TransactionID':
                    mpesa_receipt_number = item.get('Value')
                    booking.mpesa_receipt_number = mpesa_receipt_number
                    booking.payment_status = 'PAID'
                    booking.save()
                    print(f"Updated booking {booking.id} with M-Pesa receipt from callback: {mpesa_receipt_number}")
                    return True
    elif response_code == '1001':
        # Transaction still pending
        print(f"Transaction {booking.payment_reference} still pending.")
        return False
    else:
        # Other error
        print(f"Transaction {booking.payment_reference} returned response code: {response_code}")
        return False

    return False
