# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-29 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20190429_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kaohe',
            name='baogao',
            field=models.IntegerField(verbose_name='实训报告'),
        ),
        migrations.AlterField(
            model_name='kaohe',
            name='count',
            field=models.IntegerField(null=True, verbose_name='总成绩'),
        ),
        migrations.AlterField(
            model_name='kaohe',
            name='kaoqin',
            field=models.IntegerField(verbose_name='考勤'),
        ),
        migrations.AlterField(
            model_name='kaohe',
            name='shixian',
            field=models.IntegerField(verbose_name='系统实现'),
        ),
    ]