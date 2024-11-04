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
# def show_ulasan(request):
#     ulasans = Ulasan.objects.filter(user=request.user)  # Display only the logged-in user's reviews

#     context = {
#         'ulasans': ulasans,
#         'name': request.user.username,
#     }

#     return render(request, "list_ulasan.html", context)

def show_ulasan(request):
    ulasans = Ulasan.objects.all()  # Ambil semua ulasan dari database
    context = {
        'ulasans': ulasans,
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

# def create_ulasan(request):
#     if request.method == 'POST':
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ulasan:list_ulasan')
#     else:
#         form = UlasanForm()
#     return render(request, 'create_ulasan.html', {'form': form})


# def create_ulasan(request):
#     if request.method == "POST":
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save()
#             if request.is_ajax():  # Handle AJAX request
#                 return JsonResponse({
#                     "success": True,
#                     "ulasan": {
#                         "id": ulasan.id,
#                         "ulasan_makanan_souvenir": ulasan.ulasan_makanan_souvenir,
#                         "rating": ulasan.rating,
#                         "pesan_ulasan": ulasan.pesan_ulasan,
#                     }
#                 })
#             return redirect(reverse('ulasan:list_ulasan'))
#     else:
#         form = UlasanForm()
#     return render(request, 'create_ulasan.html', {'form': form})


def edit_ulasan(request, id):
    ulasan = get_object_or_404(Ulasan, pk=id)
    form = UlasanForm(request.POST or None, instance=ulasan)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('ulasan:show_ulasan'))

    context = {'form': form}
    return render(request, "edit_ulasan.html", context)

def delete_ulasan(request, id):
    ulasan = get_object_or_404(Ulasan, pk=id)
    ulasan.delete()
    return HttpResponseRedirect(reverse('ulasan:show_ulasan'))

@csrf_exempt
@require_POST
def add_ulasan_ajax(request):
    ulasan_makanan_souvenir_id = request.POST.get("ulasan_makanan_souvenir")
    rating = request.POST.get("rating")
    pesan_ulasan = strip_tags(request.POST.get("pesan_ulasan"))

    ulasan_makanan_souvenir = get_object_or_404(Katalog, pk=ulasan_makanan_souvenir_id)
    user = request.user

    new_ulasan = Ulasan(
        ulasan_makanan_souvenir=ulasan_makanan_souvenir,
        rating=rating,
        pesan_ulasan=pesan_ulasan,
        user=user
    )
    new_ulasan.save()

    return JsonResponse({"status": "success", "message": "Ulasan berhasil ditambahkan!"}, status=201)


# @csrf_exempt
# @require_POST
# def add_ulasan_ajax(request):
#     if request.method == 'POST':
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'errors': form.errors})
#     return JsonResponse({'success': False, 'message': 'Invalid request'})

# def show_json(request):
#     data = Ulasan.objects.filter(user=request.user)
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json(request):
    ulasan = Ulasan.objects.all()
    ulasan_list = list(ulasan.values('id', 'ulasan_makanan_souvenir__nama', 'rating', 'pesan_ulasan'))
    return JsonResponse(ulasan_list, safe=False)
