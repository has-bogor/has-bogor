from django.db import models

class Promo(models.Model):
    kode = models.CharField(max_length=100)
    potongan = models.FloatField()
    masa_berlaku = models.IntegerField()
    minimal_transaksi = models.FloatField()
    toko_terkait = models.ManyToManyField('Store', related_name='promos')

class Store(models.Model):
    name = models.CharField(max_length=100)
