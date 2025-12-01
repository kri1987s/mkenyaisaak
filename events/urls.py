from django.urls import path
from . import views, staff_views, api, views_test

app_name = 'events'

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/book/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/<uuid:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
    
    # Test Views
    path('<int:event_id>/book-test/', views_test.TestBookingCreateView.as_view(), name='book_test'),
    path('ticket-test/<uuid:booking_id>/', views_test.test_ticket_view, name='test_ticket'),
    
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
]
