from django.urls import path
from .views import wishlist_view, add_to_wishlist, update_wishlist, remove_from_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('my_wishlist/', wishlist_view, name='wishlist_view'),
    path('add/<int:katalog_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('update/<int:katalog_id>/', update_wishlist, name='update_wishlist'),
    path('remove/<int:katalog_id>/', remove_from_wishlist, name='remove_from_wishlist'),
]
