# Generated by Django 5.1.1 on 2024-10-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0004_alter_pembayaran_product_pembayaran_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembayaran',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pembayaran',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
