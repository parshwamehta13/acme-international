# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_goodssearch_transactionsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference_name',
            field=models.CharField(max_length=100),
        ),
    ]
