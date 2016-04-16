# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_tasksearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_detail',
            name='cash_in_hand',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True),
        ),
    ]
