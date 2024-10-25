from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nama_category = models.CharField(max_length=255)
    