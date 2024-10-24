from django import forms
from .models import Pembayaran

class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['user', 'amount', 'payment_method', 'status']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Payment Method'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
