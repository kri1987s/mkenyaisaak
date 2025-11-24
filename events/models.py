from django.db import models
from django.utils import timezone
import uuid

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to='event_posters/')
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    # Offline payment fields
    payment_till_number = models.CharField(max_length=20, blank=True, null=True, help_text="Till number for offline payment")
    payment_account_number = models.CharField(max_length=50, blank=True, null=True, help_text="Account number for bank transfers")
    payment_instructions = models.TextField(blank=True, null=True, help_text="Additional payment instructions")
    marketing_qr_code = models.ImageField(upload_to='marketing_qrs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    name = models.CharField(max_length=100) # e.g., Regular, VIP
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.event.title} - {self.name}"

class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=200, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=20)  # Required field
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    payment_reference = models.CharField(max_length=100, blank=True, null=True) # M-Pesa code
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Check if payment status changed to PAID, but only for existing bookings
        if self.pk and not self._state.adding:  # Only for existing instances, not new ones
            try:
                old_booking = Booking.objects.get(pk=self.pk)
                if old_booking.payment_status != 'PAID' and self.payment_status == 'PAID':
                    from .utils import send_ticket_confirmation_email
                    super().save(*args, **kwargs)
                    send_ticket_confirmation_email(self)
                    return
            except Booking.DoesNotExist:
                # This shouldn't normally happen if self.pk exists, but handle it gracefully
                pass

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"

class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    ticket_code = models.CharField(max_length=8, unique=True) # The 8-digit code
    qr_code = models.ImageField(upload_to='ticket_qrs/', blank=True, null=True)
    
    # Two-gate security system
    checked_in_at_gate1 = models.DateTimeField(null=True, blank=True)
    checked_in_at_gate2 = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_code}"
