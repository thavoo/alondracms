# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-01 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postitem',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
