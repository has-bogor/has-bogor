from django.contrib.auth.models import User
from django.db import models
from penyimpanan.models import Katalog

class Ulasan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ulasan_makanan_souvenir = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=((i, i) for i in range(1, 6)))  
    pesan_ulasan = models.TextField()

    def __str__(self):
        return f"{self.ulasan_makanan_souvenir.nama} - Rating: {self.rating}"