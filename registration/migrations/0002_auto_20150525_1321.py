# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='registration',
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
