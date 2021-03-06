# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-13 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
            options={
                'verbose_name_plural': '确认码',
                'ordering': ['-c_time'],
                'verbose_name': '确认码',
            },
        ),
    ]
