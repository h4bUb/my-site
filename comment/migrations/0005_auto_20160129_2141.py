# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]
