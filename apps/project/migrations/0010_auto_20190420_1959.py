# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-20 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_auto_20190420_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='select_notok',
            name='notok_stu_name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]