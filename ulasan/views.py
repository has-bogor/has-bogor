from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from .models import Ulasan
from .forms import UlasanForm
from penyimpanan.models import Katalog  # Ensure your Katalog model is imported

@login_required(login_url='/login')
def show_ulasan(request):
    ulasan = Ulasan.objects.all()
    ulasan_list = list(ulasan.values('id', 'ulasan_makanan_souvenir__nama', 'rating', 'pesan_ulasan'))
    katalog_items = Katalog.objects.all()  # Add this line
    context = {
        'ulasan_list': ulasan_list,
        'katalog_items': katalog_items,  # Add this line
    }
    return render(request, 'list_ulasan.html', context)

def create_ulasan(request):
    form = UlasanForm(request.POST or None)
    print(request.POST.get("ulasan_makanan_souvenir"))
    
    if form.is_valid() and request.method == "POST":
        ulasan = form.save(commit=False)
        ulasan.user = request.user
        ulasan.save()
        return redirect('ulasan:show_ulasan')

    katalog_items = Katalog.objects.all()  # Fetch katalog items if needed in form
    context = {
        'form': form,
        'katalog_items': katalog_items,
    }
    return render(request, "create_ulasan.html", context)


def edit_ulasan(request, id):
    ulasan = get_object_or_404(Ulasan, pk=id)
    form = UlasanForm(request.POST or None, instance=ulasan)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('ulasan:show_ulasan'))

    katalog_items = Katalog.objects.all()
    context = {
        'form': form,
        'ulasan': ulasan,
        'katalog_items': katalog_items,
    }
    return render(request, "edit_ulasan.html", context)

def delete_ulasan(request, id):
    ulasan = Ulasan.objects.get(id=id)
    ulasan.delete()
    return HttpResponseRedirect(reverse('ulasan:show_ulasan'))

@csrf_exempt
@require_POST
def add_ulasan_ajax(request):
    ulasan_makanan_souvenir_id = request.POST.get("ulasan_makanan_souvenir")
    rating = request.POST.get("rating")
    pesan_ulasan = request.POST.get("pesan_ulasan")
    user = request.user

    katalog = get_object_or_404(Katalog, pk=ulasan_makanan_souvenir_id)
    new_ulasan = Ulasan(
        ulasan_makanan_souvenir=katalog,
        rating=rating,
        pesan_ulasan=pesan_ulasan,
        user=user
    )
    new_ulasan.save()

    response_data = {
        'id': new_ulasan.id,
        'ulasan_makanan_souvenir__nama': katalog.nama,
        'rating': rating,
        'pesan_ulasan': pesan_ulasan
    }

    return JsonResponse(response_data, status=201)


def show_json(request):
    ulasan = Ulasan.objects.all()
    ulasan_list = list(ulasan.values('id', 'ulasan_makanan_souvenir__nama', 'rating', 'pesan_ulasan'))
    return JsonResponse(ulasan_list, safe=False)
