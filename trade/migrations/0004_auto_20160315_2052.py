# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20160315_2041'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goods',
            new_name='Good',
        ),
    ]
