# Generated by Django 3.0.6 on 2020-05-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0002_auto_20200531_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinasi',
            name='deskripsi',
            field=models.TextField(null=True),
        ),
    ]