from django.db import models
from django.contrib.auth.models import User
from penyimpanan.models import Katalog

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Katalog, on_delete=models.CASCADE)  
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"
