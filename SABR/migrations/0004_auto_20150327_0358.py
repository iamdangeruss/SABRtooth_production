# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SABR', '0003_master_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='master',
            old_name='fullname',
            new_name='player_fullname',
        ),
    ]
