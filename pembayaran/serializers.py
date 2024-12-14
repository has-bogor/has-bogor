# serializers.py
from rest_framework import serializers
from .models import Pembayaran
from penyimpanan.models import Katalog

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = ['id', 'amount', 'payment_method', 'total_payment', 'product']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Jumlah pembayaran harus lebih besar dari 0.")
        return value

    def validate_product(self, value):
        try:
            product = Katalog.objects.get(id=value.id)
        except Katalog.DoesNotExist:
            raise serializers.ValidationError("Produk tidak ditemukan.")
        return value
