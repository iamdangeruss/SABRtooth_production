# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0007_pitching'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fielding',
            fields=[
                ('yearid', models.IntegerField(db_column=b'yearID')),
                ('stint', models.IntegerField()),
                ('teamid', models.CharField(max_length=3, db_column=b'teamID', blank=True)),
                ('lgid', models.CharField(max_length=2, db_column=b'lgID', blank=True)),
                ('pos', models.CharField(max_length=2, db_column=b'POS')),
                ('g', models.IntegerField(null=True, db_column=b'G', blank=True)),
                ('gs', models.IntegerField(null=True, db_column=b'GS', blank=True)),
                ('innouts', models.IntegerField(null=True, db_column=b'InnOuts', blank=True)),
                ('po', models.IntegerField(null=True, db_column=b'PO', blank=True)),
                ('a', models.IntegerField(null=True, db_column=b'A', blank=True)),
                ('e', models.IntegerField(null=True, db_column=b'E', blank=True)),
                ('dp', models.IntegerField(null=True, db_column=b'DP', blank=True)),
                ('pb', models.IntegerField(null=True, db_column=b'PB', blank=True)),
                ('wp', models.IntegerField(null=True, db_column=b'WP', blank=True)),
                ('sb', models.IntegerField(null=True, db_column=b'SB', blank=True)),
                ('cs', models.IntegerField(null=True, db_column=b'CS', blank=True)),
                ('zr', models.FloatField(null=True, db_column=b'ZR', blank=True)),
                ('djangoid', models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid')),
            ],
            options={
                'db_table': 'Fielding',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
