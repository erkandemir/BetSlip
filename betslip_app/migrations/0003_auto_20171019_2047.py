# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betslip_app', '0002_auto_20171017_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
