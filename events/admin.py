from django.contrib import admin
from .models import Event, TicketType, Booking, Ticket

class TicketTypeInline(admin.TabularInline):
    model = TicketType
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'is_active')
    inlines = [TicketTypeInline]
    search_fields = ('title', 'venue')
    list_filter = ('is_active', 'date')
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description', 'poster', 'date', 'venue', 'is_active')
        }),
        ('Payment Details', {
            'fields': ('payment_till_number', 'payment_account_number', 'payment_instructions'),
            'description': 'Offline payment details for this event'
        }),
        ('Notifications', {
            'fields': ('notification_email',),
            'description': 'Email to receive booking notifications'
        }),
        ('Marketing', {
            'fields': ('marketing_qr_code',)
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'customer_phone', 'total_amount', 'payment_status_colored', 'mpesa_receipt_display', 'payment_reference', 'created_at')
    list_filter = ('payment_status', 'created_at', 'payment_reference', 'mpesa_receipt_number')
    search_fields = ('customer_name', 'customer_email', 'customer_phone', 'id', 'payment_reference', 'mpesa_receipt_number')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    # Group fields in the form
    fieldsets = (
        ('Booking Information', {
            'fields': ('id', 'customer_name', 'customer_email', 'customer_phone', 'total_amount')
        }),
        ('Payment Details', {
            'fields': ('payment_status', 'mpesa_receipt_number', 'payment_reference')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def payment_status_colored(self, obj):
        """Display payment status with visual indicators and M-Pesa receipt info"""
        if obj.mpesa_receipt_number:
            return f"✅ {obj.payment_status} ({obj.mpesa_receipt_number})"
        elif obj.payment_reference and obj.payment_status == 'PENDING':
            return f"⏳ PENDING (Ref: {obj.payment_reference[:8]}...)"
        elif obj.payment_status == 'FAILED':
            return f"❌ {obj.payment_status}"
        else:
            return f"📋 {obj.payment_status}"
    payment_status_colored.short_description = 'Payment Status'

    def mpesa_receipt_display(self, obj):
        """Display M-Pesa receipt with visual indicator if available"""
        if obj.mpesa_receipt_number:
            return f"🎯 {obj.mpesa_receipt_number}"
        else:
            return "❌ No receipt"
    mpesa_receipt_display.short_description = 'M-Pesa Receipt (Ultimate Truth)'

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'booking_customer_name', 'booking_phone', 'ticket_type', 'event_name', 'checked_in_at_gate1', 'checked_in_at_gate2', 'booking_status')
    search_fields = ('ticket_code', 'booking__customer_name', 'booking__customer_phone', 'booking__customer_email')
    list_filter = ('ticket_type__event', 'ticket_type', 'checked_in_at_gate1', 'checked_in_at_gate2', 'booking__payment_status')
    readonly_fields = ('created_at',)

    def booking_customer_name(self, obj):
        return obj.booking.customer_name
    booking_customer_name.short_description = 'Customer Name'

    def booking_phone(self, obj):
        return obj.booking.customer_phone
    booking_phone.short_description = 'Customer Phone'

    def event_name(self, obj):
        return obj.ticket_type.event.title
    event_name.short_description = 'Event'

    def booking_status(self, obj):
        return obj.booking.payment_status
    booking_status.short_description = 'Payment Status'

    # Add fieldsets for better organization
    fieldsets = (
        ('Ticket Information', {
            'fields': ('ticket_code', 'ticket_type', 'qr_code')
        }),
        ('Booking Details', {
            'fields': ('booking',)
        }),
        ('Check-in Status', {
            'fields': ('checked_in_at_gate1', 'checked_in_at_gate2')
        }),
        ('Audit', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
