# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-22 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20190422_2151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'ordering': ['date'], 'verbose_name': '文件上传', 'verbose_name_plural': '文件上传'},
        ),
        migrations.AlterModelTable(
            name='files',
            table='files_upload',
        ),
    ]
