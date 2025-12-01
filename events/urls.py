from django.urls import path
from . import views, staff_views, api, views_status, views_ticket, views_verify

app_name = 'events'

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/book/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/<uuid:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('ticket/<uuid:booking_id>/', views_ticket.ticket_view, name='ticket_view'),
    path('verify-ticket/', views_verify.verify_ticket_direct, name='verify_ticket_direct'),
    path('event/<int:event_id>/verify/', views_verify.verify_ticket_from_event, name='verify_ticket_from_event'),

    # Staff Views
    path('staff/', staff_views.StaffDashboardView.as_view(), name='staff_dashboard'),
    path('staff/event/<int:pk>/attendees/', staff_views.EventAttendeeListView.as_view(), name='staff_attendees'),
    path('staff/scanner/', staff_views.StaffScannerView.as_view(), name='staff_scanner'),
    path('staff/search/', staff_views.TicketSearchView.as_view(), name='staff_search'),
    path('staff/ticket/<int:ticket_id>/resend/', staff_views.resend_ticket_email, name='staff_resend_email'),
    
    # API
    path('api/event/<int:event_id>/attendees/', api.get_event_attendees, name='api_attendees'),
    path('api/ticket/update/', api.update_ticket_status, name='api_update_ticket'),
    path('api/verify-ticket/<str:gate_number>/', api.verify_ticket, name='api_verify_ticket'),
    path('api/payment-status/<uuid:booking_id>/', views_status.check_payment_status, name='check_payment_status'),
    path('api/payment-status-ref/', views_status.check_payment_status_by_reference, name='check_payment_status_by_reference'),
]
