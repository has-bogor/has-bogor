from django.urls import path
from penyimpanan.views import (
    show_katalog,
    add_item,
    get_item,
    get_item_by_id,
    update_item,
    delete_item,
    explore_katalog,
    katalog_list,
    add_api,
    update_api,
    delete_api
)

app_name = 'penyimpanan'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    path('add_item/', add_item, name='add_item'),
    path('get_item/', get_item, name='get_item'),
    path('get_item/<int:id>/', get_item_by_id, name='get_item_by_id'),
    path('items/<int:id>/update/', update_item, name='update_item'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('explore/', explore_katalog, name='explore'),
    path('api/katalog/', katalog_list, name='katalog_list'),
    path('api/add/', add_api, name='add_api'),
    path('api/items/<int:id>/update/', update_api, name='update_api'),
    path('api/items/<int:id>/delete/', delete_api, name='delete_api'),
]
