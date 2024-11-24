from django import forms
from django.forms import ModelForm
from .models import Ulasan
from django.utils.html import strip_tags

class UlasanForm(ModelForm):
    class Meta:
        model = Ulasan
        fields = ["ulasan_makanan_souvenir", "rating", "pesan_ulasan"]

    def clean_mood(self):
        pesan_ulasan = self.cleaned_data["pesan_ulasan"]
        return strip_tags(pesan_ulasan)

    
        