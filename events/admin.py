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

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_email', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'customer_phone', 'id')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_code', 'booking', 'ticket_type', 'checked_in_at_gate1', 'checked_in_at_gate2')
    search_fields = ('ticket_code', 'booking__customer_name')
    list_filter = ('ticket_type', 'ticket_type__event')
