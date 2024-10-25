from django import forms
from .models import Pembayaran

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['amount', 'payment_method', 'product', 'total_payment'] 
