# Generated by Django 5.1.1 on 2024-10-25 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pembayaran', '0006_alter_pembayaran_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pembayaran',
            old_name='total_payment',
            new_name='total_amount',
        ),
    ]
