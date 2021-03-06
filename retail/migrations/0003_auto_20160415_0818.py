# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0002_invoicesearch_receiptsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount_received',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
