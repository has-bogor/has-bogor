from django.urls import path
from penyimpanan.views import show_katalog, add_item, get_item, get_item_by_id, update_item, delete_item, explore_katalog, katalog_list

app_name = 'penyimpanan'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('add_item/', add_item, name='add_item'),
    path('get_item/', get_item, name='get_item'),
    path('get_item/<int:id>/', get_item_by_id, name='get_item_by_id'),
    path('update_item/', update_item, name='update_item'),
    path('delete_item/', delete_item, name='delete_item'),
    path('explore/', explore_katalog, name='explore'),
    path('api/katalog/', katalog_list, name='katalog_list'),
]