# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-14 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0019_transaction_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time_confirmed',
            field=models.DateTimeField(null=True),
        ),
    ]
