# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-05 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_schedule_select_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='select_plan',
        ),
    ]
