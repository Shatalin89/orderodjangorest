# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordermodelrest', '0006_auto_20161201_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchphoto',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images/'),
        ),
    ]
