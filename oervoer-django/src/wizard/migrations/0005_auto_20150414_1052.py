# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0004_auto_20150331_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='globals',
            name='MEAL',
            field=models.IntegerField(default=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meattype',
            name='is_gemalen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='globals',
            name='REPEATS',
            field=models.IntegerField(default=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='globals',
            name='tries',
            field=models.IntegerField(default=20),
            preserve_default=True,
        ),
    ]
