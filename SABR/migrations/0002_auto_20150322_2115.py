# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='djangoid',
            field=models.IntegerField(serialize=False, primary_key=True, db_column=b'djangoid'),
            preserve_default=True,
        ),
    ]
