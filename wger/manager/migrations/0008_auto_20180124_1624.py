# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-24 13:24
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20160311_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutsession',
            name='logs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.WorkoutLog', verbose_name='Workout Log'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='reps',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(600)], verbose_name='Amount'),
        ),
    ]
