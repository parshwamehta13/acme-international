# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-25 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_employee_detail_cash_in_hand'),
        ('logistics', '0004_auto_20160309_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='homepage.Employee_Detail'),
        ),
    ]
