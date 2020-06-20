# Generated by Django 3.0.6 on 2020-05-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinasi',
            name='link',
        ),
        migrations.AddField(
            model_name='destinasi',
            name='maplink',
            field=models.TextField(default='<img href="https://via.placeholder.com/600x400.jpg?text=belum+ada+map"'),
        ),
        migrations.AddField(
            model_name='destinasi',
            name='thumbnail',
            field=models.TextField(default='https://via.placeholder.com/300x200.jpg?text=tidak+ada+gambar'),
        ),
        migrations.AddField(
            model_name='destinasi',
            name='weblink',
            field=models.TextField(default='<a href="#"></a>'),
        ),
    ]
