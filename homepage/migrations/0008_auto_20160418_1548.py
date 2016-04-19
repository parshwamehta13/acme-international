# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20160415_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesearch',
            name='employeesearch_type',
            field=models.CharField(choices=[('salary', 'Salary'), ('cash_in_hand', 'Cash In Hand')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tasksearch',
            name='tasksearch_type',
            field=models.CharField(choices=[('task_description', 'Task Description'), ('assigned_on', 'Assigned on'), ('deadline', 'Deadline'), ('status', 'Status'), ('priority', 'Priority')], max_length=20),
        ),
    ]