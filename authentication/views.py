from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from penyimpanan.models import Katalog  


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
    user_profile = UserProfile.objects.get(user=request.user)
    katalog_items = Katalog.objects.all()

    context = {
        'user_profile': user_profile,
        'katalog_items': katalog_items, 
    }
    
    return render(request, 'home.html', context)

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('authentication:login')