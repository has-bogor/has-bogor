from django import forms
from .models import Katalog

class AddBookForm(forms.Form):
   class Meta:
       model = Katalog
       fields = ['nama', 'kategori', 'harga', 'deskripsi', 'toko']