# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0002_auto_20150322_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='fullname',
            field=models.CharField(max_length=50, db_column=b'fullname', blank=True),
            preserve_default=True,
        ),
    ]
