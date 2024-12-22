# penyimpanan/models.py
from django.db import models
from category.models import Category

class Katalog(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.IntegerField()
    deskripsi = models.TextField() 
    toko = models.CharField(max_length=100) 

    def __str__(self):
        return self.nama