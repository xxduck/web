# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-08 09:09
from __future__ import unicode_literals

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_notice_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cninfo',
            fields=[
                ('num', models.IntegerField(max_length=10)),
                ('short_name', models.TextField()),
                ('title', models.CharField(max_length=15)),
                ('href', models.IntegerField(primary_key=builtins.id, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
