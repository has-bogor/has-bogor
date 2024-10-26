# urls.py di dalam aplikasi katalog
from django.urls import path
from .views import explore_katalog  # Import view yang baru dibuat

app_name = 'penyimpanan'

urlpatterns = [
    path('explore/', explore_katalog, name='explore'),
]
