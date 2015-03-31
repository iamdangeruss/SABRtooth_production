# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0006_master_player_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('stint', models.IntegerField()),
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
            ],
            options={
                'db_table': 'Pitching',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
