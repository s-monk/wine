# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-01 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('web', models.URLField()),
                ('phone', models.CharField(max_length=200)),
                ('salesman', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='wine',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='wine',
            name='distributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='distributors', to='wineapp.Distributor'),
        ),
    ]
