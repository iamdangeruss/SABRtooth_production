# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0009_battingpost_fieldingpost_pitchingpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamsfranchises',
            fields=[
                ('franchid', models.CharField(max_length=3, serialize=False, primary_key=True, db_column=b'franchID')),
                ('franchname', models.CharField(max_length=50, db_column=b'franchName', blank=True)),
                ('active', models.CharField(max_length=2, blank=True)),
                ('naassoc', models.CharField(max_length=3, db_column=b'NAassoc', blank=True)),
            ],
            options={
                'db_table': 'TeamsFranchises',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
