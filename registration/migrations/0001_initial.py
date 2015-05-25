# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('last_name', models.CharField(verbose_name='last name', max_length=32)),
                ('first_name', models.CharField(verbose_name='first name', max_length=32)),
                ('patronymic', models.CharField(verbose_name='patronymic', max_length=32)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(verbose_name='city', max_length=32)),
                ('street', models.CharField(verbose_name='street', max_length=32)),
                ('house', models.IntegerField(verbose_name='house')),
                ('house_fraction', models.IntegerField(verbose_name='fraction', blank=True)),
                ('appartment', models.IntegerField(verbose_name='appartment')),
                ('index', models.IntegerField(verbose_name='index')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('login', models.CharField(verbose_name='login:', max_length=32, unique=True)),
                ('email', models.EmailField(verbose_name='email', max_length=32, unique=True)),
                ('password', models.CharField(verbose_name='password', null=True, max_length=32)),
                ('repeat_password', models.CharField(verbose_name='repeat password', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(to='registration.Registration'),
        ),
    ]
