# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160411_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecashbook',
            name='transaction_details',
            field=models.TextField(blank=True),
        ),
    ]
