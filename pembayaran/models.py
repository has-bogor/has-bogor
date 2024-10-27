from django.db import models
from penyimpanan.models import Katalog

class Pembayaran(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Katalog, on_delete=models.CASCADE)  # Mengaitkan produk
    status = models.CharField(max_length=20, default='Success')
    created_at = models.DateTimeField(auto_now_add=True)
    
    PAYMENT_METHOD_CHOICES = [
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('e_wallet', 'E-Wallet'),
        ('ovo', 'OVO'),               # Tambahkan pilihan baru sesuai form
        ('gopay', 'GoPay'),           # Tambahkan pilihan baru sesuai form
        ('dana', 'Dana'),             # Tambahkan pilihan baru sesuai form
        ('linkaja', 'LinkAja'),       # Tambahkan pilihan baru sesuai form
    ]
    
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD_CHOICES, default='bank_transfer')
    amount = models.IntegerField()               # Jumlah produk yang dibeli
    total_payment = models.IntegerField()        # Total pembayaran (jumlah x harga)

    def __str__(self):
        return f"Pembayaran untuk {self.product.nama} - Jumlah: {self.amount} ({self.status})"
