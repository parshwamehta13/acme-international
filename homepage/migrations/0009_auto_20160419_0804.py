# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20160418_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_detail',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
