# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-08 01:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordermodelrest', '0008_auto_20161207_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchphoto',
            name='idmerch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='ordermodelrest.Merchandise'),
        ),
    ]
