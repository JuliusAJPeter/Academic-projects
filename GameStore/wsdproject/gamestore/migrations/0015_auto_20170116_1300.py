# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0014_auto_20170116_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(),
        ),
    ]
