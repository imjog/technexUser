# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-11 21:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0065_auto_20170108_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbReach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=200, null=True)),
                ('accessToken', models.CharField(max_length=250, null=True)),
                ('profileImage', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]
