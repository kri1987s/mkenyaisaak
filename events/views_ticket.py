from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Booking

@require_http_methods(["GET"])
def ticket_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'events/ticket.html', {'booking': booking})