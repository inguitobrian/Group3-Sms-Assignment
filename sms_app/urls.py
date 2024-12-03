# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('send_sms/', views.send_sms_view, name='send_sms'),  
]
