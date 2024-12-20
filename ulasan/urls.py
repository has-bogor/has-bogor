from django.urls import path
from ulasan.views import * 

app_name = 'ulasan'

urlpatterns = [
    path('create/', create_ulasan, name='create_ulasan'),  
    path('show_ulasan', show_ulasan, name='show_ulasan'),  
    path('delete/<int:id>/', delete_ulasan, name='delete_ulasan'),   
    path('edit-ulasan/<int:id>/', edit_ulasan, name='edit_ulasan'),
    path('json/', show_json, name='show_json'),  
    path('list-ulasan-ajax', add_ulasan_ajax, name='add_ulasan_ajax'),
    path('show-katalogs/', show_katalogs, name='show_katalogs'),
    path('delete/flutter/', delete_ulasan_flutter, name="delete_ulasan_flutter"),
    path('create/flutter/', create_ulasan_flutter, name='create_ulasan_flutter'),
    path('edit/flutter/<int:id>/', edit_ulasan_flutter, name='edit_ulasan_flutter'),
]


