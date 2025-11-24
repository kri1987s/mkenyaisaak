from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from core.mixins import StaffRequiredMixin
from .models import Event, Ticket

class StaffDashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'events/staff/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(is_active=True).order_by('date')
        return context

class EventAttendeeListView(StaffRequiredMixin, DetailView):
    model = Event
    template_name = 'events/staff/attendee_list.html'
    context_object_name = 'event'

class StaffScannerView(StaffRequiredMixin, TemplateView):
    template_name = 'events/staff/scanner.html'

class TicketSearchView(StaffRequiredMixin, TemplateView):
    template_name = 'events/staff/ticket_search.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if request.headers.get('HX-Request') and query:
            tickets = Ticket.objects.filter(
                Q(booking__customer_name__icontains=query) | 
                Q(booking__customer_phone__icontains=query) |
                Q(ticket_code__icontains=query)
            ).select_related('booking', 'ticket_type__event')[:10]
            return render(request, 'events/staff/partials/search_results.html', {'tickets': tickets})
        return super().get(request, *args, **kwargs)

def resend_ticket_email(request, ticket_id):
    if not request.user.is_staff:
        raise PermissionDenied
    
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    from .utils import send_ticket_confirmation_email
    send_ticket_confirmation_email(ticket.booking)
    
    messages.success(request, f"Email resent to {ticket.booking.customer_email}")
    return redirect('events:staff_search')
