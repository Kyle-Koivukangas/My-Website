# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 04:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171129_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 11, 29, 20, 18, 37, 610390)),
        ),
    ]
