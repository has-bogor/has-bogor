from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from category.models import Category
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from penyimpanan.models import Katalog  
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            UserProfile.objects.create(user=user)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)  
            if user is not None:
                auth_login(request, user)
                return redirect('authentication:home')  
            else:
                messages.error(request, 'Invalid username or password.')  
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'login.html')


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  
    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)

@login_required 
def home(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    katalog_items = Katalog.objects.all()
    for item in katalog_items:
        item.category_name = item.kategori  # Default to the category ID
        try:
            category = Category.objects.get(id=item.kategori)
            item.category_name = category.nama_category  # Fetch category name
        except Category.DoesNotExist:
            item.category_name = 'Category not found'


    context = {
        'user_profile': user_profile,
        'katalog_items': katalog_items, 
    }
    
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('authentication:login')

@csrf_exempt
def api_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                "is_superuser": user.is_superuser
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali username atau kata sandi."
        }, status=401)
    

@csrf_exempt
def katalog_list(request):
    katalogs = Katalog.objects.all()
    katalog_data = []
    
    for katalog in katalogs:
        item_data = {
            'id': katalog.id,
            'nama': katalog.nama,
            'kategori': katalog.kategori,
            'harga': katalog.harga,
            'deskripsi': katalog.deskripsi,
            'toko': katalog.toko,
        }
        
        try:
            category = Category.objects.get(id=katalog.kategori)
            item_data['category_name'] = category.nama_category
        except Category.DoesNotExist:
            item_data['category_name'] = 'Category not found'
            
        katalog_data.append(item_data)
    
    return JsonResponse(katalog_data, safe=False)

@csrf_exempt
def api_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)