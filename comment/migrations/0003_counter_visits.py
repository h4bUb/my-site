# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20160129_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='visits',
            field=models.IntegerField(default=1),
        ),
    ]
