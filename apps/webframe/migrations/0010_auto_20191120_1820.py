# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-21 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webframe', '0009_auto_20191120_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedetect',
            name='img',
            field=models.ImageField(upload_to='~/ml'),
        ),
    ]