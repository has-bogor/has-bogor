from django.db import models

class Katalog(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.CharField(max_length=50)  
    deskripsi = models.TextField() 
    toko = models.CharField(max_length=100) 

    def __str__(self):
        return self.nama 
    
class User(models.Model): 
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username