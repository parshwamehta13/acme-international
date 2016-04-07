# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20160407_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_mode',
            field=models.CharField(choices=[('Cheque', 'Cheque'), ('Cash', 'Cash')], default='Cash', max_length=30),
        ),
    ]
