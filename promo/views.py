from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from promo.models import Promo
from promo.forms import PromoForm
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from authentication.models import UserProfile

@login_required(login_url="authentication:login")
def show_promo(request):
    user = request.user
    context = {"user": user}

    if request.user.is_superuser:
        return render(request, "promo.html", context)

    return render(request, 'customer_promo.html', context)

def create_promo(request):
    form = PromoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('promo:show_promo')
    
    context = {'form': form}
    return render(request, "create_promo.html", context)

def edit_promo(request, id):
    promo = Promo.objects.get(pk=id)

    form = PromoForm(request.POST or None, instance=promo)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('promo:show_promo'))
    
    context = {'form': form}
    return render(request, "edit_promo.html", context)

def delete_promo(request, id):
    promo = Promo.objects.get(pk = id)

    promo.delete()

    return HttpResponseRedirect(reverse('promo:show_promo'))

def show_json(request):
    data = Promo.objects.all()
    print("Data fetched:", data)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
@require_POST
def add_related_store(request, id):
    try:
        promo = Promo.objects.get(pk=id)
        new_store = json.loads(request.body)
        
        # Assuming `toko_terkait` is a JSONField
        related_stores = promo.toko_terkait or []
        related_stores.append(new_store)  # Add new store to the list
        promo.toko_terkait = related_stores
        promo.save()
        
        return JsonResponse({'status': 'success', 'related_stores': promo.toko_terkait})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt 
@require_POST
def remove_related_store(request, id):
    try:
        promo = Promo.objects.get(pk=id)
        storeName = json.loads(request.body).get('storeName')
        
        # Remove the store from the list
        related_stores = promo.toko_terkait
        related_stores = [store for store in related_stores if store.get('name') != storeName]
        promo.toko_terkait = related_stores
        promo.save()
        
        return JsonResponse({'status': 'success', 'related_stores': promo.toko_terkait})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def show_filtered_promo(request):
    sort_by = request.GET.get("sort_by", "tanpa_filter")

    if sort_by == "tanpa_filter":
        promos = Promo.objects.all()
    elif sort_by == "masa_berlaku":
        promos = Promo.objects.all().order_by("masa_berlaku")  # Ascending order for expiration date
    elif sort_by == "potongan":
        promos = Promo.objects.all().order_by("-potongan")  # Descending order for discount

    return HttpResponse(serializers.serialize("json", promos), content_type="application/json")

@csrf_exempt
def create_promo_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_promo = Promo.objects.create(
                kode=data["kode"],  # String
                potongan=float(data["potongan"]),  # Float
                masa_berlaku=int(data["masa_berlaku"]),  # Integer
                minimal_transaksi=float(data["minimal_transaksi"]),  # Float
                toko_terkait=[]  # Empty list for JSONField
            )

            new_promo.save()

            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=401)

@csrf_exempt
def edit_promo_flutter(request, id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            promo = Promo.objects.get(pk=id)
            
            promo.kode = data["kode"]
            promo.potongan = float(data["potongan"])
            promo.masa_berlaku = int(data["masa_berlaku"])
            promo.minimal_transaksi = float(data["minimal_transaksi"])
            
            promo.save()

            return JsonResponse({"status": "success"}, status=200)
        except Promo.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Promo not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    else:
        return JsonResponse({"status": "error", "message": "Invalid method"}, status=401)