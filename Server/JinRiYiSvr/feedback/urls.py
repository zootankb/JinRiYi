from django.apps import AppConfig
from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'photoWeb'


urlpatterns = [
    path('start_feedback/', start_feedback, name='start_feedback'),
    path('get_verification_code/', get_verification_code, name='get_verification_code'),
    path('check_verification_valid/', check_verification_valid, name='check_verification_valid'),
    path('get_all_products/', get_all_products, name='get_all_products'),
]
