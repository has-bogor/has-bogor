from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from penyimpanan.models import Katalog
from django.contrib import messages
from django.contrib.auth.models import User

# coba make dummy user
def add_to_wishlist_for_dummy_user(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    dummy_user = User.objects.get(username='dummyuser')
    wishlist_item, created = Wishlist.objects.get_or_create(user=dummy_user, product=katalog)

    if created:
        messages.success(request, f"{katalog.name} has been added to dummy user's wishlist.")
    else:
        messages.info(request, f"{katalog.name} is already in dummy user's wishlist.")

    return redirect('wishlist_view')

def add_to_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item, created = Wishlist.objects.get_or_create(product=katalog)

    if created:
        messages.success(request, f"{katalog.name} has been added to your wishlist.")
    else:
        messages.info(request, f"{katalog.name} is already in your wishlist.")

    return redirect('wishlist_view')

def remove_from_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item = Wishlist.objects.filter(product=katalog).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"{katalog.name} has been removed from your wishlist.")
    else:
        messages.warning(request, f"{katalog.name} was not found in your wishlist.")

    return redirect('wishlist_view')

def wishlist_view(request):
    dummy_user = User.objects.get(username='dummyuser')
    wishlist_items = Wishlist.objects.filter(user=dummy_user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})