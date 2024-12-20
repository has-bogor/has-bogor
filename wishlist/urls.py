from django.urls import path
from .views import wishlist_view, add_to_wishlist, update_wishlist, remove_from_wishlist, add_to_wishlist_ajax, fetch_wishlist, add_wishlist_flutter, delete_wishlist_flutter

app_name = 'wishlist'

urlpatterns = [
    path('my_wishlist/', wishlist_view, name='wishlist_view'),
    path('add/<int:katalog_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('update/<int:katalog_id>/', update_wishlist, name='update_wishlist'),
    path('remove/<int:katalog_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/add-to-wishlist-ajax/', add_to_wishlist_ajax, name='add_to_wishlist_ajax'),
    path('json/', fetch_wishlist, name='fetch_wishlist'),
    path('api/add/<int:katalog_id>/', add_wishlist_flutter, name='add_wishlist_flutter'),
    path('api/remove/<int:katalog_id>/', delete_wishlist_flutter, name='delete_wishlist_flutter'),
]
