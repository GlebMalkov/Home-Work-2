# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 20:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0003_auto_20170104_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='regdate',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='follows',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
