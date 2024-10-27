from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_POST
from .models import Ulasan
from .forms import UlasanForm
# from django.contrib.auth.decorators import login_required
from penyimpanan.models import Katalog


# def list_ulasan(request):
#     ulasans = Ulasan.objects.all()
#     katalog_items = Katalog.objects.all()  
#     form = UlasanForm()
#     return render(request, 'list_ulasan.html', {
#         'ulasans': ulasans,
#         'form': form,
#         'katalog_items': katalog_items
#     })


# views.py
# def list_ulasan(request):
#     ulasans = Ulasan.objects.all()
#     # Data dummy untuk testing tanpa migrasi
#     katalog_items = [
#         {"pk": 1, "nama": "Asinan Bogor", "kategori": "Makanan"},
#         {"pk": 2, "nama": "Roti Unyil Venus", "kategori": "Makanan"},
#         {"pk": 3, "nama": "Talas Bogor", "kategori": "Makanan"}
#     ]
#     form = UlasanForm()
#     return render(request, 'list_ulasan.html', {
#         'ulasans': ulasans,
#         'form': form,
#         'katalog_items': katalog_items
#     })

# def list_ulasan(request):
#     ulasans = Ulasan.objects.all()
#     katalog_items = Katalog.objects.all()  
#     return render(request, 'list_ulasan.html', {
#         'ulasans': ulasans,
#         'katalog_items': katalog_items,
#     })


# def list_ulasan(request):
#     ulasans = Ulasan.objects.select_related('ulasan_makanan_souvenir').all()
#     return render(request, "list_ulasan.html", {"ulasans": ulasans})

def list_ulasan(request):
    ulasans = Ulasan.objects.select_related('ulasan_makanan_souvenir').all()
    
    return render(request, 'list_ulasan.html', {
        'ulasans': ulasans,
    })

# @login_required
# def create_ulasan(request):
#     if request.method == "POST":
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user
#             ulasan.save()
#             return JsonResponse({"status": "success", "message": "Ulasan berhasil ditambahkan"})
#         else:
#             return JsonResponse({"status": "error", "errors": form.errors})
#     return JsonResponse({"status": "error", "message": "Invalid request"})

# @login_required
# def create_ulasan(request):
#     if request.method == "POST":
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user
#             ulasan.save()
#             return JsonResponse({
#                 "status": "success",
#                 "message": "Ulasan berhasil ditambahkan",
#                 "ulasan": {
#                     "user": ulasan.user.username,
#                     "rating": ulasan.rating,
#                     "pesan_ulasan": ulasan.pesan_ulasan,
#                     "nama": ulasan.ulasan_makanan_souvenir.nama,
#                 }
#             })
#         else:
#             print("Form errors:", form.errors)  
#             return JsonResponse({"status": "error", "errors": form.errors}, status=400)
#     print("Non-POST request received") 
#     return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

# def create_ulasan(request):
#     if request.method == "POST":
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user  
#             ulasan.save()
#             return redirect('ulasan:list_ulasan')  
#         else:
#             print("Form errors:", form.errors)  
#             return render(request, 'create_ulasan.html', {'form': form, 'errors': form.errors})
#     else:
#         form = UlasanForm()
#     return render(request, 'create_ulasan.html', {'form': form})

# def create_ulasan(request):
#     if request.method == "POST":
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user
#             ulasan.save()
#             return redirect('ulasan:list_ulasan')
#     else:
#         form = UlasanForm()
        
#     katalog_items = [
#         {"pk": 1, "nama": "Asinan Bogor", "kategori": "Makanan"},
#         {"pk": 2, "nama": "Roti Unyil Venus", "kategori": "Makanan"},
#         {"pk": 3, "nama": "Talas Bogor", "kategori": "Makanan"}
#     ]
    
#     return render(request, 'create_ulasan.html', {
#         'form': form,
#         'katalog_items': katalog_items
#     })


# def create_ulasan(request):
#     if request.method == 'POST':
#         form = UlasanForm(request.POST)
#         if form.is_valid():
#             ulasan = form.save(commit=False)
#             ulasan.user = request.user  # Pastikan ini di-set jika diperlukan
#             ulasan.save()
#             return redirect('ulasan:list_ulasan')
#     else:
#         form = UlasanForm()
#     return render(request, 'create_ulasan.html', {'form': form})

def create_ulasan(request):
    if request.method == "POST":
        ulasan_makanan_souvenir_id = request.POST.get("ulasan_makanan_souvenir")
        rating = request.POST.get("rating")
        pesan_ulasan = request.POST.get("pesan_ulasan")
        
        user = User.objects.first()  

        try:
            ulasan_makanan_souvenir = Katalog.objects.get(pk=ulasan_makanan_souvenir_id)
        except Katalog.DoesNotExist:
            return redirect("ulasan:create_ulasan")

        Ulasan.objects.create(
            user=user,
            ulasan_makanan_souvenir=ulasan_makanan_souvenir,
            rating=rating,
            pesan_ulasan=pesan_ulasan,
        )

        return redirect("ulasan:list_ulasan")
    
    katalog_items = Katalog.objects.all()
    return render(request, "create_ulasan.html", {"katalog_items": katalog_items})

@require_POST
def delete_ulasan(request, pk):
        if request.method == "DELETE":
            ulasan = get_object_or_404(Ulasan, pk=pk)
            ulasan.delete()
            return JsonResponse({'status': 'success', 'message': 'Ulasan berhasil dihapus!'})
        else:
            return HttpResponseNotAllowed(['DELETE'])

def edit_ulasan(request, pk):
    ulasan = get_object_or_404(Ulasan, pk=pk)
    katalog_items = Katalog.objects.all()  

    if request.method == "POST":
        form = UlasanForm(request.POST, instance=ulasan)
        if form.is_valid():
            form.save()
            return redirect("ulasan:list_ulasan")
    else:
        form = UlasanForm(instance=ulasan)

    return render(request, "edit_ulasan.html", {
        "form": form,
        "ulasan": ulasan,
        "katalog_items": katalog_items,  
    })

def show_json(request):
    ulasans = Ulasan.objects.all().values('pk', 'user_username', 'rating', 'pesan_ulasan')
    ulasan_list = list(ulasans)  
    return JsonResponse(ulasan_list, safe=False)

# def list_ulasan_json(request):
#     ulasans = Ulasan.objects.all().values('ulasan_makanan_souvenir__nama', 'rating', 'pesan_ulasan')
#     ulasan_list = list(ulasans)  
#     return JsonResponse(ulasan_list, safe=False)


def list_ulasan_json(request):
    ulasans = Ulasan.objects.select_related('ulasan_makanan_souvenir').all()
    ulasan_data = [
        {
            'ulasan_makanan_souvenir__nama': ulasan.ulasan_makanan_souvenir.nama,
            'rating': ulasan.rating,
            'pesan_ulasan': ulasan.pesan_ulasan,
        } for ulasan in ulasans
    ]
    print("Ulasan data:", ulasan_data)  
    return JsonResponse(ulasan_data, safe=False)

def get_katalog_items(request):
    katalog_items = Katalog.objects.all().values('id', 'nama')
    return JsonResponse(list(katalog_items), safe=False)