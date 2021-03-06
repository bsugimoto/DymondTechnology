# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-13 06:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume/')),
                ('interests', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Project Manager', 'Project Manager'), ('Project Scheduler', 'Project Scheduler'), ('Information Technology Analyst', 'Information Technology Analyst'), ('Information Technology Engineer', 'Information Technology Engineer'), ('Information Technology Programmer', 'Information Technology Programmer'), ('Information Technology Architect', 'Information Technology Architect')], max_length=163, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
