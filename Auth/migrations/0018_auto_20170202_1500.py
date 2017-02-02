# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-02 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0017_auto_20170202_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizTeam2',
            fields=[
                ('teamId', models.AutoField(primary_key=True, serialize=False)),
                ('quizTeamId', models.CharField(blank=True, max_length=10, null=True)),
                ('quizAttemptStatus', models.SmallIntegerField(default=0)),
                ('slot', models.SmallIntegerField(default=0)),
                ('member1Email', models.CharField(blank=True, max_length=65, null=True)),
                ('member2Email', models.CharField(blank=True, max_length=65, null=True)),
                ('member1Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('member2Phone', models.CharField(blank=True, max_length=15, null=True)),
                ('name1', models.CharField(blank=True, max_length=50, null=True)),
                ('name2', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False)),
                ('quiz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.quiz')),
            ],
        ),
        migrations.RemoveField(
            model_name='quizteam',
            name='member1Email',
        ),
        migrations.RemoveField(
            model_name='quizteam',
            name='member2Email',
        ),
        migrations.AlterField(
            model_name='quizteam',
            name='members',
            field=models.ManyToManyField(null=True, related_name='quizMembers', to='Auth.TechProfile'),
        ),
    ]
