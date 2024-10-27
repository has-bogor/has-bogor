from django import forms
from .models import Pembayaran

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['amount', 'payment_method', 'product', 'total_payment']
        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Masukkan Jumlah'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-input'}),
        } 