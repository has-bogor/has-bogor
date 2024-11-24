from django.db import models
import uuid

class Promo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kode = models.CharField(max_length=100)
    potongan = models.FloatField()
    masa_berlaku = models.IntegerField()
    minimal_transaksi = models.FloatField()
    toko_terkait = models.JSONField(default=list)
