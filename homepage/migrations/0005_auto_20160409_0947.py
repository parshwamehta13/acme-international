# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_task_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employeesearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_search_item', models.CharField(max_length=300)),
                ('employeesearch_type', models.CharField(choices=[('salary', 'Salary'), ('user', 'Employee name')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('Urgent', 'Urgent'), ('Normal Priority', 'Normal Priority'), ('Low Priority', 'Low Priority')], default='Normal Priority', max_length=20),
        ),
    ]