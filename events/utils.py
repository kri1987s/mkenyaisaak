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
