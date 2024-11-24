from django import forms
from .models import Pembayaran

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        # Hanya ambil 'amount', 'payment_method', dan 'total_payment' dari form
        fields = ['amount', 'payment_method', 'total_payment']  

        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Masukkan Jumlah'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }
