# Generated by Django 5.1.2 on 2024-10-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0003_alter_promo_minimal_transaksi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='minimal_transaksi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
