from django.urls import path
from ulasan.views import *

app_name = 'ulasan'

urlpatterns = [
    path('create/', create_ulasan, name='create_ulasan'),  
    path('show_ulasan', show_ulasan, name='show_ulasan'),  
    path('delete/<int:pk>/', delete_ulasan, name='delete_ulasan'),  
    path('edit/<int:pk>/', edit_ulasan, name='edit_ulasan'), 
    path('json/', show_json, name='show_json'),  
    path('list_json/', add_ulasan_ajax, name='list_ulasan_json'),  
    path('list-ulasan-ajax', add_ulasan_ajax, name='add_ulasan_ajax')
]
