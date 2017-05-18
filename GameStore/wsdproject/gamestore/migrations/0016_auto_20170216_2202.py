# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0015_auto_20170116_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('time_confirmed', models.DateTimeField(null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_games', to='gamestore.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='developed_games', to='gamestore.UserProfile'),
        ),
        migrations.AlterField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('AC', 'Action'), ('AD', 'Adventure'), ('AR', 'Arcade'), ('PZ', 'Puzzle'), ('RC', 'Racing'), ('SH', 'Shooting'), ('SP', 'Sports'), ('OT', 'Other')], default='OT', max_length=2),
        ),
        migrations.AddField(
            model_name='transaction',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='gamestore.Game'),
        ),
    ]
