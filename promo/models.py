from django.db import models
import uuid

class Promo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode = models.CharField(max_length=255)
    potongan = models.IntegerField()
    masa_berlaku = models.CharField(max_length=255)
    minimal_transaksi = models.IntegerField()
    toko_terkait = models.JSONField(default=list)