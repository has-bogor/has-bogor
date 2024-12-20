from django.urls import path
from promo.views import *
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
    path('create-promo-flutter/', create_promo_flutter, name='create_promo_flutter'),
    path('edit-promo-flutter/<uuid:id>/', edit_promo_flutter, name='edit_promo_flutter'),
    path('delete-flutter/<uuid:id>/', delete_promo_flutter, name='delete_promo_flutter'),
    path('add-store-flutter/<uuid:id>/', add_store_flutter, name='add_store_flutter'),
    path('remove-store-flutter/<uuid:id>/', remove_store_flutter, name='remove_store_flutter'),
]