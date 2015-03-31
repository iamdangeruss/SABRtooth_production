# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0005_remove_master_player_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='player_fullname',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
