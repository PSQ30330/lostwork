# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-17 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20190417_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='register_num',
        ),
    ]
