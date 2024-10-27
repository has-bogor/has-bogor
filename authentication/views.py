from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Register
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')  

        if form.is_valid():
            user = form.save()  # Simpan pengguna yang sudah divalidasi
            UserProfile.objects.create(user=user, user_type=user_type)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Error in form submission. Please check your inputs.')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

# Login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Mengambil username dari form
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)  # Menggunakan username
            if user is not None:
                auth_login(request, user)
                return redirect('authentication:home')  # Redirect ke halaman home setelah login
            else:
                messages.error(request, 'Invalid username or password.')  # Mengubah pesan kesalahan
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'login.html')


# Profile (protected view)
@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  
    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)

# Home (protected view)
@login_required
def home(request):
    context = {
        'user_profile': UserProfile.objects.get(user=request.user)
    }
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('authentication:login')