# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-21 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgin', '0003_auto_20190421_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='sgin',
            name='beizhu',
            field=models.CharField(max_length=100, null=True, verbose_name='备注'),
        ),
    ]
