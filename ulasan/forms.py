from django import forms
from django.forms import ModelForm
from .models import Ulasan

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ["ulasan_makanan_souvenir", "rating", "pesan_ulasan"]
        