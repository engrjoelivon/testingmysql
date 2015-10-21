# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usersinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('interests', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'UserInfo',
            },
        ),
    ]
