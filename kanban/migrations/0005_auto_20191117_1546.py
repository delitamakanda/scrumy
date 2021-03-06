# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-11-17 14:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0004_auto_20191117_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 14, 46, 13, 8013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='card',
            name='tag',
            field=models.CharField(choices=[('#BEE3F8', 'Bug'), ('#FED7D7', 'Feature Request'), ('#EDF2F7', 'Marketing'), ('#FEEBC8', 'v2.0'), ('#C6F6D5', 'Enhancement'), ('#FED7E2', 'Design')], default='#BEE3F8', max_length=7),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
