from django.urls import path
from authentication.models import HomeView
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('home/', home, name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('api/login/', login, name='api_login'),
]
