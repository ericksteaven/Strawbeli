# Generated by Django 3.0.6 on 2020-05-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='link_galeri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinasi', models.CharField(max_length=50)),
                ('link', models.TextField()),
            ],
        ),
    ]
