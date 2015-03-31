# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0004_auto_20150327_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='player_fullname',
        ),
    ]
