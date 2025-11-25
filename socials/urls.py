from django.urls import path
from . import views

app_name = 'socials'

urlpatterns = [
    path('', views.socials_index, name='index'),
]