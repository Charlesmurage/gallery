# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0004_uploader_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdetails',
            name='photo_image',
            field=models.ImageField(default='DEFAULT', upload_to='photos/'),
        ),
    ]