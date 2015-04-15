# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizard', '0002_auto_20150210_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='profile',
            field=models.ForeignKey(default=1, to='wizard.Globals'),
            preserve_default=False,
        ),
    ]
