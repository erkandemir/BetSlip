# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betslip_app', '0004_auto_20171019_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betslip',
            name='matches',
            field=models.ManyToManyField(to='betslip_app.Match'),
        ),
    ]
