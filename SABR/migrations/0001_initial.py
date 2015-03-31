# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('stint', models.IntegerField()),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID', blank=True)),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID', blank=True)),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
                ('g_batting', models.IntegerField(null=True, db_column=b'G_batting', blank=True)),
                ('ab', models.IntegerField(null=True, db_column=b'AB', blank=True)),
                ('r', models.IntegerField(null=True, db_column=b'R', blank=True)),
                ('h', models.IntegerField(null=True, db_column=b'H', blank=True)),
                ('number_2b', models.IntegerField(null=True, db_column=b'2B', blank=True)),
                ('number_3b', models.IntegerField(null=True, db_column=b'3B', blank=True)),
                ('hr', models.IntegerField(null=True, db_column=b'HR', blank=True)),
                ('rbi', models.IntegerField(null=True, db_column=b'RBI', blank=True)),
                ('sb', models.IntegerField(null=True, db_column=b'SB', blank=True)),
                ('cs', models.IntegerField(null=True, db_column=b'CS', blank=True)),
                ('bb', models.IntegerField(null=True, db_column=b'BB', blank=True)),
                ('so', models.IntegerField(null=True, db_column=b'SO', blank=True)),
                ('ibb', models.IntegerField(null=True, db_column=b'IBB', blank=True)),
                ('hbp', models.IntegerField(null=True, db_column=b'HBP', blank=True)),
                ('sh', models.IntegerField(null=True, db_column=b'SH', blank=True)),
                ('sf', models.IntegerField(null=True, db_column=b'SF', blank=True)),
                ('gidp', models.IntegerField(null=True, db_column=b'GIDP', blank=True)),
                ('g_old', models.IntegerField(null=True, db_column=b'G_old', blank=True)),
                ('djangoid', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'Batting',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('playerid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column=b'playerID')),
                ('birthyear', models.IntegerField(null=True, db_column=b'birthYear', blank=True)),
                ('birthmonth', models.IntegerField(null=True, db_column=b'birthMonth', blank=True)),
                ('birthday', models.IntegerField(null=True, db_column=b'birthDay', blank=True)),
                ('birthcountry', models.CharField(max_length=50, db_column=b'birthCountry', blank=True)),
                ('birthstate', models.CharField(max_length=2, db_column=b'birthState', blank=True)),
                ('birthcity', models.CharField(max_length=50, db_column=b'birthCity', blank=True)),
                ('deathyear', models.IntegerField(null=True, db_column=b'deathYear', blank=True)),
                ('deathmonth', models.IntegerField(null=True, db_column=b'deathMonth', blank=True)),
                ('deathday', models.IntegerField(null=True, db_column=b'deathDay', blank=True)),
                ('deathcountry', models.CharField(max_length=50, db_column=b'deathCountry', blank=True)),
                ('deathstate', models.CharField(max_length=2, db_column=b'deathState', blank=True)),
                ('deathcity', models.CharField(max_length=50, db_column=b'deathCity', blank=True)),
                ('namefirst', models.CharField(max_length=50, db_column=b'nameFirst', blank=True)),
                ('namelast', models.CharField(max_length=50, db_column=b'nameLast', blank=True)),
                ('namegiven', models.CharField(max_length=255, db_column=b'nameGiven', blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('bats', models.CharField(max_length=1, blank=True)),
                ('throws', models.CharField(max_length=1, blank=True)),
                ('debut', models.DateTimeField(null=True, blank=True)),
                ('finalgame', models.DateTimeField(null=True, db_column=b'finalGame', blank=True)),
                ('retroid', models.CharField(max_length=9, db_column=b'retroID', blank=True)),
                ('bbrefid', models.CharField(max_length=9, db_column=b'bbrefID', blank=True)),
            ],
            options={
                'db_table': 'Master',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='batting',
            name='playerid',
            field=models.ForeignKey(to='SABR.Master'),
            preserve_default=True,
        ),
    ]
