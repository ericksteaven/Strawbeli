# Generated by Django 3.0.6 on 2020-06-06 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20200607_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='dagangan',
            name='gambar_barang',
            field=models.TextField(default='via.placeholder.com/500x500.jpg?text=no+image'),
        ),
    ]
