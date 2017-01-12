# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-08 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0062_auto_20170108_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='collegeWebsite',
            field=models.CharField(default='0', max_length=250),
        ),
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]
