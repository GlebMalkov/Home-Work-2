# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bullet',
            name='tmp_follow',
            field=models.ManyToManyField(related_name='_bullet_tmp_follow_+', to='bulletin.Bullet'),
        ),
    ]