# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-19 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webframe', '0003_auto_20191119_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='img',
            field=models.ImageField(upload_to='static/webframe/images'),
        ),
    ]