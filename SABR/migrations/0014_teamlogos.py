# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0013_technologies_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLogos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamid', models.CharField(max_length=3)),
                ('image', models.ImageField(null=True, upload_to=b'teams', blank=True)),
                ('startyear', models.IntegerField(null=True, blank=True)),
                ('endyear', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
