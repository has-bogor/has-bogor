from django.forms import ModelForm
from promo.models import Promo

class PromoForm(ModelForm):
    class Meta:
        model = Promo
        fields = ["kode", "potongan", "masa_berlaku", "minimal_transaksi"]