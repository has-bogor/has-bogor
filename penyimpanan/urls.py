# urls.py di dalam aplikasi katalog
from django.urls import path
from .views import explore_katalog, katalog_list

app_name = 'penyimpanan'

urlpatterns = [
    path('explore/', explore_katalog, name='explore'),
    path('api/katalog/', katalog_list, name='katalog_list'),
]