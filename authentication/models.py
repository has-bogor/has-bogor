from django.db import models
from django.contrib.auth.models import User
from penyimpanan.models import Katalog
from django.views import View
from django.shortcuts import render

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')