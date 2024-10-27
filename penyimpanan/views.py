from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import Katalog
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core import serializers

# Create your views here.
@login_required(login_url="authentication:login")
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
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_item(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_item_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def update_item(request, id):
    item = Katalog.objects.get(pk=id)
    if request.method == "POST":
        new_nama = request.POST.get("nama")
        new_kategori = request.POST.get("kategori")
        new_harga = request.POST.get("harga")
        new_deskripsi = request.POST.get("deskripsi")
        new_toko = request.POST.get("toko")
        item.nama = new_nama
        item.kategori = new_kategori
        item.harga = new_harga
        item.deskripsi = new_deskripsi
        item.toko = new_toko
        item.save()
        return HttpResponse(b"UPDATED", status=200)
    
def delete_item(request, id):
    item = Katalog.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('katalog:show_katalog'))