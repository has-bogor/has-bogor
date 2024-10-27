from django.urls import path
from promo.views import show_promo, create_promo, edit_promo, delete_promo, show_json, add_related_store, remove_related_store, show_filtered_promo

app_name = 'promo'

urlpatterns = [
    path('', show_promo, name='show_promo'),
    path('create-promo', create_promo, name='create_promo'),
    path('edit-promo/<uuid:id>', edit_promo, name='edit_promo'),
    path('delete/<uuid:id>', delete_promo, name='delete_promo'),
    path('show_json', show_json, name='show_json'),
    path('add_store/<uuid:id>/', add_related_store, name='add_store'),
    path('remove_store/<uuid:id>/', remove_related_store, name='remove_store'),
    path('filtered/', show_filtered_promo, name='show_filtered_promo'),
]