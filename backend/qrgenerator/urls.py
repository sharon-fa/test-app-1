from django.urls import path
from .views import qr_code_generator, home

app_name = 'qrgenerator'

urlpatterns = [
    path('', home, name='home'),
    path('generate/', qr_code_generator, name='qr_code_generator'),
]
