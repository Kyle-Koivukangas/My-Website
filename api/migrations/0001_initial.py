# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('project_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='uploads')),
            ],
        ),
    ]
