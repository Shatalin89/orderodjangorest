# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermodelrest', '0004_auto_20161130_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchphoto',
            name='image',
            field=models.ImageField(default='images/none/mo_img.jpg', max_length=255, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]