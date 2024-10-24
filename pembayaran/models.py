from django.db import models
from penyimpanan.models import Katalog

class Pembayaran(models.Model):  
    product = models.ForeignKey(Katalog, on_delete=models.CASCADE, default=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Pembayaran untuk {self.product.name} - {self.amount} ({self.status})"
