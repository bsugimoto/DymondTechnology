# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0002_auto_20180412_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='opportunity',
            name='organization',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
