# Generated by Django 5.1.1 on 2024-10-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_category', models.CharField(max_length=255)),
            ],
        ),
    ]
