# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocontent',
            name='file',
        ),
        migrations.AddField(
            model_name='videocontent',
            name='url',
            field=models.URLField(default='youtube.com'),
            preserve_default=False,
        ),
    ]
