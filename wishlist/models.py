from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from wishlist.models import Product  # Asumsikan kamu sudah punya model Product


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Pastikan Product sudah ada di modelmu
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"

