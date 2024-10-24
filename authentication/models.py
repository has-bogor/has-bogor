from django.db import models
from django.contrib.auth.models import User
from penyimpanan.models import Katalog

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10)