from django.urls import path
from ulasan.views import* 

app_name = 'ulasan'  
urlpatterns = [
    path('', list_ulasan, name='list_ulasan'),
    path('create_ulasan/', create_ulasan, name='create_ulasan'),
    path('delete_ulasan/<int:pk>/', delete_ulasan, name='delete_ulasan'),
    path('edit/<int:pk>/', edit_ulasan, name='edit_ulasan'),
    path('ulasan/json/', show_json, name='show_json'),  
    path('list_ulasan_json/', list_ulasan_json, name='list_ulasan_json'),
    path('get_katalog_items/', get_katalog_items, name='get_katalog_items'),
]
