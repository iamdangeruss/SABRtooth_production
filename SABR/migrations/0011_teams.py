# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0010_teamsfranchises'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID')),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID')),
                ('divid', models.CharField(max_length=1, db_column=b'divID', blank=True)),
                ('rank', models.IntegerField(null=True, db_column=b'Rank', blank=True)),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
                ('ghome', models.IntegerField(null=True, db_column=b'Ghome', blank=True)),
                ('w', models.IntegerField(null=True, db_column=b'W', blank=True)),
                ('l', models.IntegerField(null=True, db_column=b'L', blank=True)),
                ('divwin', models.CharField(max_length=1, db_column=b'DivWin', blank=True)),
                ('wcwin', models.CharField(max_length=1, db_column=b'WCWin', blank=True)),
                ('lgwin', models.CharField(max_length=1, db_column=b'LgWin', blank=True)),
                ('wswin', models.CharField(max_length=1, db_column=b'WSWin', blank=True)),
                ('r', models.IntegerField(null=True, db_column=b'R', blank=True)),
                ('ab', models.IntegerField(null=True, db_column=b'AB', blank=True)),
                ('h', models.IntegerField(null=True, db_column=b'H', blank=True)),
                ('number_2b', models.IntegerField(null=True, db_column=b'2B', blank=True)),
                ('number_3b', models.IntegerField(null=True, db_column=b'3B', blank=True)),
                ('hr', models.IntegerField(null=True, db_column=b'HR', blank=True)),
                ('bb', models.IntegerField(null=True, db_column=b'BB', blank=True)),
                ('so', models.IntegerField(null=True, db_column=b'SO', blank=True)),
                ('sb', models.IntegerField(null=True, db_column=b'SB', blank=True)),
                ('cs', models.IntegerField(null=True, db_column=b'CS', blank=True)),
                ('hbp', models.IntegerField(null=True, db_column=b'HBP', blank=True)),
                ('sf', models.IntegerField(null=True, db_column=b'SF', blank=True)),
                ('ra', models.IntegerField(null=True, db_column=b'RA', blank=True)),
                ('er', models.IntegerField(null=True, db_column=b'ER', blank=True)),
                ('era', models.FloatField(null=True, db_column=b'ERA', blank=True)),
                ('cg', models.IntegerField(null=True, db_column=b'CG', blank=True)),
                ('sho', models.IntegerField(null=True, db_column=b'SHO', blank=True)),
                ('sv', models.IntegerField(null=True, db_column=b'SV', blank=True)),
                ('ipouts', models.IntegerField(null=True, db_column=b'IPouts', blank=True)),
                ('ha', models.IntegerField(null=True, db_column=b'HA', blank=True)),
                ('hra', models.IntegerField(null=True, db_column=b'HRA', blank=True)),
                ('bba', models.IntegerField(null=True, db_column=b'BBA', blank=True)),
                ('soa', models.IntegerField(null=True, db_column=b'SOA', blank=True)),
                ('e', models.IntegerField(null=True, db_column=b'E', blank=True)),
                ('dp', models.IntegerField(null=True, db_column=b'DP', blank=True)),
                ('fp', models.FloatField(null=True, db_column=b'FP', blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('park', models.CharField(max_length=255, blank=True)),
                ('attendance', models.IntegerField(null=True, blank=True)),
                ('bpf', models.IntegerField(null=True, db_column=b'BPF', blank=True)),
                ('ppf', models.IntegerField(null=True, db_column=b'PPF', blank=True)),
                ('teamidbr', models.CharField(max_length=3, db_column=b'teamIDBR', blank=True)),
                ('teamidlahman45', models.CharField(max_length=3, db_column=b'teamIDlahman45', blank=True)),
                ('teamidretro', models.CharField(max_length=3, db_column=b'teamIDretro', blank=True)),
                ('djangoid', models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid')),
            ],
            options={
                'db_table': 'Teams',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
