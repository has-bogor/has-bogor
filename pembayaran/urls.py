from django.urls import path
from .views import create_payment, payment_history, update_payment, delete_payment

app_name = 'pembayaran'

urlpatterns = [
    path('create/', create_payment, name='create'),
    path('history/', payment_history, name='payment_history'),
    path('update/<int:payment_id>/', update_payment, name='update_payment'),
    path('delete/<int:payment_id>/', delete_payment, name='delete_payment'),
]
