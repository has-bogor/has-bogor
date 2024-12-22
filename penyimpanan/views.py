from .models import Katalog
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from penyimpanan.forms import AddItemForm
from django.contrib import messages

# @login_required(login_url="authentication:login")
def show_katalog(request):
    user = request.user
    items = Katalog.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'item.html', context)

@csrf_exempt
@require_POST
def add_item(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        kategori = request.POST.get("kategori")
        harga = request.POST.get("harga")
        deskripsi = request.POST.get("deskripsi")
        toko = request.POST.get("toko")

        new_item = Katalog(nama=nama, kategori=kategori, harga=harga, deskripsi=deskripsi, toko=toko)
        new_item.save()
        return redirect('penyimpanan:show_katalog')
    return HttpResponseNotFound()

def get_item(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_item_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def update_item(request, id):
    item = get_object_or_404(Katalog, pk=id)

    if request.method == 'POST':
        form = AddItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('penyimpanan:show_katalog')  # Redirect hanya jika berhasil
    else:
        form = AddItemForm(instance=item)

    # Jika request GET atau form tidak valid, tampilkan halaman form edit
    return render(request, 'penyimpanan/edit_item.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Katalog.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('penyimpanan:show_katalog'))

def explore_katalog(request):
    search_query = request.GET.get('search', '')
    if search_query:
        katalog_items = Katalog.objects.filter(nama__icontains=search_query)  # Gunakan model Katalog
    else:
        katalog_items = Katalog.objects.all()
    
    return render(request, 'penyimpanan/explore_katalog.html', {'katalog_items': katalog_items})

def katalog_list(request):
    katalog = list(Katalog.objects.values('id', 'nama', 'harga', 'kategori', 'deskripsi', 'toko'))
    for item in katalog:
        item['harga'] = float(item['harga'])
    return JsonResponse(katalog, safe=False)

@csrf_exempt
def add_api(request):
    if request.method == "POST":
        try:
            # Parse JSON payload
            data = json.loads(request.body)

            # Extract fields
            nama = data.get("nama")
            kategori = data.get("kategori")
            harga = data.get("harga")
            deskripsi = data.get("deskripsi")
            toko = data.get("toko")

            # Validate fields
            if not all([nama, kategori, harga, deskripsi, toko]):
                return JsonResponse({"error": "All fields are required."}, status=400)

            # Save new item
            new_item = Katalog(
                nama=nama,
                kategori=kategori,
                harga=harga,
                deskripsi=deskripsi,
                toko=toko,
            )
            new_item.save()
            print(nama, kategori, harga, deskripsi, toko)

            # Return success response
            return JsonResponse({"message": "Item added successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)

@csrf_exempt
def update_api(request, id):
    try:
        # Retrieve the item to be updated
        item = Katalog.objects.get(pk=id)
    except Katalog.DoesNotExist:
        return JsonResponse({"error": "Item not found"}, status=404)

    if request.method == "POST":
        try:
            # Parse the JSON body
            data = json.loads(request.body)

            # Update item fields
            item.nama = data.get("nama", item.nama)
            item.harga = data.get("harga", item.harga)
            item.kategori = data.get("kategori", item.kategori)
            item.deskripsi = data.get("deskripsi", item.deskripsi)
            item.toko = data.get("toko", item.toko)

            # Save the updated item
            item.save()
            return JsonResponse({"message": "Item updated successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)

@csrf_exempt
def delete_api(request, id):
    if request.method == 'POST':  # Use DELETE HTTP method for deletions
        item = get_object_or_404(Katalog, pk=id)
        item.delete()
        return JsonResponse({"message": "Item deleted successfully"}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=400)