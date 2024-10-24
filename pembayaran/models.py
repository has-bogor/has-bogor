from django.db import models

class Produk(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Pembayaran(models.Model):  
    product = models.ForeignKey(Produk, on_delete=models.CASCADE, default=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')  # Status pembayaran
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pembayaran untuk {self.product.name} - {self.amount} ({self.status})"
