# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-14 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190413_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='has_confirmed',
            field=models.BooleanField(default=False, verbose_name='激活状态'),
        ),
    ]
