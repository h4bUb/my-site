# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20160129_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
