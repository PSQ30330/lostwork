# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-17 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_remove_student_register_num'),
        ('project', '0002_auto_20190416_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=32, verbose_name='姓名')),
                ('stu_major', models.CharField(max_length=15, verbose_name='专业')),
                ('stu_class', models.CharField(max_length=15, verbose_name='班级')),
                ('stu_protitle', models.CharField(max_length=40, verbose_name='实训题目')),
                ('stu_teacher', models.CharField(max_length=15, verbose_name='指导老师')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='选题时间')),
                ('stu_proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.TeacherProject')),
                ('stu_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'verbose_name': '学生选题',
                'db_table': 'student_select',
                'ordering': ['-c_time'],
                'verbose_name_plural': '学生选题',
            },
        ),
    ]