# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_registration_date_filed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='house_fraction',
            field=models.IntegerField(verbose_name='fraction', null=True, blank=True),
        ),
    ]
