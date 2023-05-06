# Generated by Django 4.2 on 2023-05-06 06:42

import ImagesApp.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ImagesApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image_field',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=ImagesApp.models.getfilename),
            preserve_default=False,
        ),
    ]
