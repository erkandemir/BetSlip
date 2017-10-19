# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BetSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tournament_name', models.CharField(max_length=100)),
                ('market_name', models.CharField(max_length=100)),
                ('total_bet', models.FloatField()),
                ('possibiltiy', models.FloatField(null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('market_name', models.CharField(max_length=100)),
                ('bet', models.FloatField()),
                ('start_date', models.FloatField()),
                ('tournament_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='betslip',
            name='matches',
            field=models.ManyToManyField(related_name='match', to='betslip_app.Match'),
        ),
    ]