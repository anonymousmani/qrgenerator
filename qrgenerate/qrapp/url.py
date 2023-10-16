from django.urls import path
from qrapp import views

urlpatterns = [
    path('', views.generate_qr_code, name='generate_qr_code'),
    path('download_qr_code/', views.download_qr_code, name='download_qr_code')
]
