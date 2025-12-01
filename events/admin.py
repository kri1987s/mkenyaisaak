from django.contrib import admin
from django.http import HttpResponse
from .models import Event, TicketType, Booking, Ticket
import csv

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
    list_display = ('id', 'customer_name', 'customer_email', 'customer_phone', 'total_amount', 'payment_status_display', 'mpesa_receipt_number_display', 'mpesa_transaction_date_display', 'payment_reference', 'created_at')
    list_filter = ('payment_status', 'created_at', 'mpesa_transaction_date', 'payment_reference', 'mpesa_receipt_number', 'customer_phone')
    search_fields = ('customer_name', 'customer_email', 'customer_phone', 'id', 'payment_reference', 'mpesa_receipt_number')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    actions = ['export_bookings_csv']

    # Group fields in the form
    fieldsets = (
        ('Booking Information', {
            'fields': ('id', 'customer_name', 'customer_email', 'customer_phone', 'total_amount')
        }),
        ('Payment Details', {
            'fields': ('payment_status', 'mpesa_receipt_number', 'mpesa_transaction_date', 'payment_reference')
        }),
        ('Audit', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def payment_status_display(self, obj):
        """Display payment status with M-Pesa receipt info"""
        base_status = obj.payment_status

        if obj.mpesa_receipt_number:
            if obj.mpesa_transaction_date:
                return f"{base_status} ({obj.mpesa_receipt_number}) on {obj.mpesa_transaction_date}"
            else:
                return f"{base_status} ({obj.mpesa_receipt_number})"
        elif obj.payment_reference and obj.payment_status == 'PENDING':
            return f"PENDING (Ref: {obj.payment_reference[:8]}...)"
        else:
            return base_status
    payment_status_display.short_description = 'Payment Status'

    def mpesa_receipt_number_display(self, obj):
        """Display M-Pesa receipt if available"""
        if obj.mpesa_receipt_number:
            return obj.mpesa_receipt_number
        else:
            return "No receipt"
    mpesa_receipt_number_display.short_description = 'M-Pesa Receipt'

    def mpesa_transaction_date_display(self, obj):
        """Display M-Pesa transaction date if available"""
        if obj.mpesa_transaction_date:
            # Format the date for better readability (if it's in YYYYMMDDHHMMSS format)
            date_str = obj.mpesa_transaction_date
            if len(date_str) == 14:  # YYYYMMDDHHMMSS format
                try:
                    # Parse the date string and format it nicely
                    parsed_date = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]} {date_str[8:10]}:{date_str[10:12]}:{date_str[12:14]}"
                    return parsed_date
                except:
                    return date_str  # Return original if parsing fails
            return date_str
        else:
            return "No date"
    mpesa_transaction_date_display.short_description = 'M-Pesa Transaction Date'

    def export_bookings_csv(self, request, queryset):
        """Export selected bookings to CSV"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="bookings.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'ID', 'Customer Name', 'Customer Email', 'Customer Phone',
            'Total Amount', 'Payment Status', 'M-Pesa Receipt',
            'M-Pesa Transaction Date', 'Payment Reference', 'Created At'
        ])

        for booking in queryset:
            # Format date for CSV export as well
            formatted_date = booking.mpesa_transaction_date
            if formatted_date and len(formatted_date) == 14:
                try:
                    formatted_date = f"{formatted_date[0:4]}-{formatted_date[4:6]}-{formatted_date[6:8]} {formatted_date[8:10]}:{formatted_date[10:12]}:{formatted_date[12:14]}"
                except:
                    pass  # Keep original if formatting fails

            writer.writerow([
                booking.id, booking.customer_name, booking.customer_email,
                booking.customer_phone, booking.total_amount, booking.payment_status,
                booking.mpesa_receipt_number, formatted_date,
                booking.payment_reference, booking.created_at
            ])

        return response
    export_bookings_csv.short_description = "Export selected bookings as CSV"

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'booking_customer_name', 'booking_phone', 'ticket_type', 'event_name', 'mpesa_receipt_number_display', 'mpesa_transaction_date_display', 'checked_in_at_gate1', 'checked_in_at_gate2', 'booking_status')
    search_fields = ('ticket_code', 'booking__customer_name', 'booking__customer_phone', 'booking__customer_email', 'booking__customer_name__icontains')
    list_filter = ('ticket_type__event', 'ticket_type', 'checked_in_at_gate1', 'checked_in_at_gate2', 'booking__payment_status', 'booking__mpesa_transaction_date', 'booking__customer_phone')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    actions = ['export_tickets_csv']

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

    def mpesa_receipt_number_display(self, obj):
        receipt = obj.booking.mpesa_receipt_number
        if receipt:
            return receipt
        else:
            return "No receipt"
    mpesa_receipt_number_display.short_description = 'M-Pesa Receipt'

    def mpesa_transaction_date_display(self, obj):
        """Display M-Pesa transaction date if available"""
        if obj.booking.mpesa_transaction_date:
            # Format the date for better readability (if it's in YYYYMMDDHHMMSS format)
            date_str = obj.booking.mpesa_transaction_date
            if len(date_str) == 14:  # YYYYMMDDHHMMSS format
                try:
                    # Parse the date string and format it nicely
                    parsed_date = f"{date_str[0:4]}-{date_str[4:6]}-{date_str[6:8]} {date_str[8:10]}:{date_str[10:12]}:{date_str[12:14]}"
                    return parsed_date
                except:
                    return date_str  # Return original if parsing fails
            return date_str
        else:
            return "No date"
    mpesa_transaction_date_display.short_description = 'M-Pesa Transaction Date'

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

    def export_tickets_csv(self, request, queryset):
        """Export selected tickets to CSV"""
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="tickets.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Ticket Code', 'Customer Name', 'Customer Phone', 'Ticket Type',
            'Event Name', 'M-Pesa Receipt', 'M-Pesa Transaction Date', 'Checked In Gate 1',
            'Checked In Gate 2', 'Payment Status', 'Created At'
        ])

        for ticket in queryset:
            # Format date for CSV export as well
            formatted_date = ticket.booking.mpesa_transaction_date
            if formatted_date and len(formatted_date) == 14:
                try:
                    formatted_date = f"{formatted_date[0:4]}-{formatted_date[4:6]}-{formatted_date[6:8]} {formatted_date[8:10]}:{formatted_date[10:12]}:{formatted_date[12:14]}"
                except:
                    pass  # Keep original if formatting fails

            writer.writerow([
                ticket.ticket_code, ticket.booking.customer_name,
                ticket.booking.customer_phone, ticket.ticket_type.name,
                ticket.ticket_type.event.title, ticket.booking.mpesa_receipt_number,
                formatted_date, ticket.checked_in_at_gate1, ticket.checked_in_at_gate2,
                ticket.booking.payment_status, ticket.created_at
            ])

        return response
    export_tickets_csv.short_description = "Export selected tickets as CSV"
