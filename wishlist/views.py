from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from penyimpanan.models import Katalog
from django.contrib import messages
from django.contrib.auth.models import User


def add_to_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=katalog)

    if created:
        messages.success(request, f"{katalog.nama} has been added to your wishlist.")
    else:
        messages.info(request, f"{katalog.nama} is already in your wishlist.")

    return redirect('wishlist:wishlist_view')

def wishlist_view(request):
    print("Wishlist view accessed")  # This should appear in your server logs
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

def update_wishlist(request, katalog_id):
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product_id=katalog_id)
    if request.method == 'POST':
        new_katalog_id = request.POST.get('new_product_id')
        new_katalog = get_object_or_404(Katalog, id=new_katalog_id)
        wishlist_item.product = new_katalog
        wishlist_item.save()
        messages.success(request, f"Wishlist updated to {new_katalog.nama}.")
        return redirect('wishlist:wishlist_view')
    return render(request, 'wishlist/update_wishlist.html', {'wishlist_item': wishlist_item})

def remove_from_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=katalog).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"{katalog.nama} has been removed from your wishlist.")
    else:
        messages.warning(request, f"{katalog.nama} was not found in your wishlist.")

    return redirect('wishlist:wishlist_view')
