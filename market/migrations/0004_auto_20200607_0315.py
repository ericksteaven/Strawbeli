# Generated by Django 3.0.6 on 2020-06-06 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0003_dagangan_keranjang'),
    ]

    operations = [
        migrations.AddField(
            model_name='dagangan',
            name='harga_barang',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dagangan',
            name='kategori_barang',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='dagangan',
            name='penjual',
            field=models.ForeignKey(default='default', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username', unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Keranjang',
        ),
    ]
