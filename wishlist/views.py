import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist
from penyimpanan.models import Katalog
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse

def add_to_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=katalog)

    if created:
        messages.success(request, f"{katalog.nama} has been added to your wishlist.")
    else:
        messages.info(request, f"{katalog.nama} is already in your wishlist.")

    # return redirect('wishlist:wishlist_view')

def add_to_wishlist_ajax(request: HttpRequest):
    print(request.body)  # Debugging statement
    if request.method == 'POST':
        print("AJAX request received")  # Confirming AJAX request
        
        # Parse the JSON data
        data = json.loads(request.body)
        print("Data received:", data)  # Print received data

        # Get the product_id from the data
        product_id = data.get('product_id')

        # Retrieve the Katalog (product) item, assuming `Katalog` is the model for products
        katalog = None
        try:
            katalog = Katalog.objects.get(id=product_id)
        except Katalog.DoesNotExist:
            return JsonResponse({"success": False, "message": "Product not found"}, status=404)

        # Create or get the Wishlist item for the user
        already_have = Wishlist.objects.filter(user = request.user, product = katalog)
        
        if already_have:
            return JsonResponse({"success": True, "message": "Item already in wishlist"})
        
        created = Wishlist.objects.create(user = request.user, product = katalog)
        return JsonResponse({"success": True, "message": "Item added to wishlist"})
    
    # print("Request not as expected")  # For non-AJAX or non-POST cases
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)




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
