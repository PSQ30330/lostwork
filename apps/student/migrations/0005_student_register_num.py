# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-17 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20190416_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='register_num',
            field=models.IntegerField(max_length=1000, null=True, verbose_name='注册人数'),
        ),
    ]
