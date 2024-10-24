from django import forms
from .models import Pembayaran

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['product', 'amount', 'status']  