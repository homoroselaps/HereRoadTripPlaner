# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('x', models.IntegerField(verbose_name='Coordinate X')),
                ('y', models.IntegerField(verbose_name='Coordinate Y')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('cities', models.ForeignKey(to='planer.City')),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('drivingPerDay', models.IntegerField(verbose_name='in hours')),
                ('totalDays', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='settings',
            field=models.ForeignKey(to='planer.UserSettings'),
        ),
    ]
