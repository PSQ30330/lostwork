# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-13 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_confirmstring'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=128, validators=['密', '码']),
        ),
    ]