# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('config', jsonfield.fields.JSONField()),
            ],
        ),
    ]