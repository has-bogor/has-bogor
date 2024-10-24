# Generated by Django 5.1.1 on 2024-10-24 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='pembayaran',
            old_name='payment_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='user',
        ),
        migrations.AlterField(
            model_name='pembayaran',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='pembayaran',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pembayaran.produk'),
        ),
    ]