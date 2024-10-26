from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserProfile  # Import model UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')  # Ambil user_type dari form

        if password == confirm_password:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = username  # Set username
                user.email = email  # Set email jika Anda menginginkan
                user.save()
                user_profile = UserProfile.objects.create(user=user, user_type=user_type)  # Set user_type dari dropdown
                messages.success(request, 'Your account has been successfully created!')
                return redirect('authentication:login')
        else:
            messages.error(request, 'Passwords do not match.')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f'Email: {email}, Password: {password}')  # Tambahkan ini
        if email and password:
            user = authenticate(request, username=email, password=password)
            print(f'User: {user}')  # Tambahkan ini
            if user is not None:
                auth_login(request, user)
                return redirect('authentication:home')
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'login.html')

def logout(request):  # Ubah nama fungsi menjadi logout_view
    auth_logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('authentication:login')

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)  
    context = {'user_profile': user_profile}
    return render(request, 'profile.html', context)

@login_required
def home(request):
    context = {
        'user_profile': UserProfile.objects.get(user=request.user)
    }
    return render(request, 'home.html')