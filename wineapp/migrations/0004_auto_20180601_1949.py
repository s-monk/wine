# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-01 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0003_auto_20180601_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='distributor',
            field=models.ForeignKey(blank=True, default='distributor', on_delete=django.db.models.deletion.CASCADE, related_name='distributors', to='wineapp.Distributor'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='importer',
            field=models.ForeignKey(blank=True, default='importer', on_delete=django.db.models.deletion.CASCADE, related_name='importers', to='wineapp.Importer'),
        ),
    ]
