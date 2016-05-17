# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adaptive_engine_app', '0003_auto_20160429_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='version',
        ),
        migrations.RemoveField(
            model_name='version',
            name='component',
        ),
        migrations.DeleteModel(
            name='Component',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
        migrations.DeleteModel(
            name='Version',
        ),
    ]
