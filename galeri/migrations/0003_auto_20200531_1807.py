# Generated by Django 3.0.6 on 2020-05-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0002_link_galeri'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeri',
            name='tag',
            field=models.CharField(default='slave', max_length=10),
        ),
        migrations.AlterField(
            model_name='galeri',
            name='link360',
            field=models.TextField(default='https://via.placeholder.com/600x400.jpg?text=nopic'),
        ),
    ]
