from django.db import models
# from category.models import Category

# Create your models here.

class Katalog(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    kategori = models.CharField(max_length=100)
    # kategori = models.ManyToManyField(Category, on_delete=models.CASCADE)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    toko = models.CharField(max_length=100)