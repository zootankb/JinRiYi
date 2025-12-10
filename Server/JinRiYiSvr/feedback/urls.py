from django.apps import AppConfig
from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'photoWeb'


urlpatterns = [
    path('', index, name='index'),
    path('start_feedback/', start_feedback, name='start_feedback'),
    path('get_verification_code/', get_verification_code, name='get_verification_code'),
    path('check_verification_valid/', check_verification_valid, name='check_verification_valid'),
    path('get_all_products/', get_all_products, name='get_all_products'),
    path('get_hot_products/', get_hot_products, name='get_hot_products'),
    path('get_products/', get_products, name='get_products'),
    path('get_main_data/', get_main_data, name='get_main_data'),
    path('download_image/<path:filename>/', download_image, name='download_image'),
]
