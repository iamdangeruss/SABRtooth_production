# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0008_fielding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battingpost',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('round', models.CharField(max_length=10)),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID', blank=True)),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID', blank=True)),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
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
                ('djangoid', models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid')),
            ],
            options={
                'db_table': 'BattingPost',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fieldingpost',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID', blank=True)),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID', blank=True)),
                ('round', models.CharField(max_length=10)),
                ('pos', models.CharField(max_length=2, db_column=b'POS')),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
                ('gs', models.IntegerField(null=True, db_column=b'GS', blank=True)),
                ('innouts', models.IntegerField(null=True, db_column=b'InnOuts', blank=True)),
                ('po', models.IntegerField(null=True, db_column=b'PO', blank=True)),
                ('a', models.IntegerField(null=True, db_column=b'A', blank=True)),
                ('e', models.IntegerField(null=True, db_column=b'E', blank=True)),
                ('dp', models.IntegerField(null=True, db_column=b'DP', blank=True)),
                ('tp', models.IntegerField(null=True, db_column=b'TP', blank=True)),
                ('pb', models.IntegerField(null=True, db_column=b'PB', blank=True)),
                ('sb', models.IntegerField(null=True, db_column=b'SB', blank=True)),
                ('cs', models.IntegerField(null=True, db_column=b'CS', blank=True)),
                ('djangoid', models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid')),
            ],
            options={
                'db_table': 'FieldingPost',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pitchingpost',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('round', models.CharField(max_length=10)),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID', blank=True)),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID', blank=True)),
                ('w', models.IntegerField(null=True, db_column=b'W', blank=True)),
                ('l', models.IntegerField(null=True, db_column=b'L', blank=True)),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
                ('gs', models.IntegerField(null=True, db_column=b'GS', blank=True)),
                ('cg', models.IntegerField(null=True, db_column=b'CG', blank=True)),
                ('sho', models.IntegerField(null=True, db_column=b'SHO', blank=True)),
                ('sv', models.IntegerField(null=True, db_column=b'SV', blank=True)),
                ('ipouts', models.IntegerField(null=True, db_column=b'IPouts', blank=True)),
                ('h', models.IntegerField(null=True, db_column=b'H', blank=True)),
                ('er', models.IntegerField(null=True, db_column=b'ER', blank=True)),
                ('hr', models.IntegerField(null=True, db_column=b'HR', blank=True)),
                ('bb', models.IntegerField(null=True, db_column=b'BB', blank=True)),
                ('so', models.IntegerField(null=True, db_column=b'SO', blank=True)),
                ('baopp', models.FloatField(null=True, db_column=b'BAOpp', blank=True)),
                ('era', models.FloatField(null=True, db_column=b'ERA', blank=True)),
                ('ibb', models.IntegerField(null=True, db_column=b'IBB', blank=True)),
                ('wp', models.IntegerField(null=True, db_column=b'WP', blank=True)),
                ('hbp', models.IntegerField(null=True, db_column=b'HBP', blank=True)),
                ('bk', models.IntegerField(null=True, db_column=b'BK', blank=True)),
                ('bfp', models.IntegerField(null=True, db_column=b'BFP', blank=True)),
                ('gf', models.IntegerField(null=True, db_column=b'GF', blank=True)),
                ('r', models.IntegerField(null=True, db_column=b'R', blank=True)),
                ('sh', models.IntegerField(null=True, db_column=b'SH', blank=True)),
                ('sf', models.IntegerField(null=True, db_column=b'SF', blank=True)),
                ('gidp', models.IntegerField(null=True, db_column=b'GIDP', blank=True)),
                ('djangoid', models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid')),
            ],
            options={
                'db_table': 'PitchingPost',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
