# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-20 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_article_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='numread',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='numsay',
            field=models.IntegerField(default=0),
        ),
    ]
