# penyimpanan/views.py

from django.shortcuts import render
from .models import Katalog  # Perbarui import untuk menggunakan model Katalog

def explore_katalog(request):
    search_query = request.GET.get('search', '')
    if search_query:
        katalog_items = Katalog.objects.filter(nama__icontains=search_query)  # Gunakan model Katalog
    else:
        katalog_items = Katalog.objects.all()
    
    return render(request, 'penyimpanan/explore_katalog.html', {'katalog_items': katalog_items})
