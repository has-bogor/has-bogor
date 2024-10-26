from django.urls import path
from .views import wishlist_view, add_to_wishlist_for_dummy_user, remove_from_wishlist

urlpatterns = [
    path('my_wishlist/', wishlist_view, name='wishlist_view'),
    path('add/<int:katalog_id>/', add_to_wishlist_for_dummy_user, name='add_to_wishlist_for_dummy_user'),
    path('remove_from_wishlist/<int:katalog_id>/', remove_from_wishlist, name='remove_from_wishlist'),
]