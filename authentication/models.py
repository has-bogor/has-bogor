from django.db import models
from django.contrib.auth.models import User
from penyimpanan.models import Katalog
from django.views import View
from django.shortcuts import render

# Create your models here.
class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

    
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')