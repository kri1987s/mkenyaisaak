from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.EventListView.as_view(), name='event_list'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/book/', views.BookingCreateView.as_view(), name='booking_create'),
    path('booking/<uuid:booking_id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
