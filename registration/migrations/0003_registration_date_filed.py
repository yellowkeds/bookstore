# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20150525_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='date_filed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
