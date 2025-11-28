from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.initiate_payment, name='mpesa_initiate'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
]
