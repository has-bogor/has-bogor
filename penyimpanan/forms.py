
from django import forms
from .models import Katalog

class AddItemForm(forms.ModelForm): 
    class Meta:
        model = Katalog
        fields = ['nama', 'harga', 'kategori', 'deskripsi', 'toko']
