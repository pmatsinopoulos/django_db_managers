# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpinionPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default=None, max_length=255, unique=True)),
                ('poll_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'polls_opinion_polls',
            },
        ),
    ]
