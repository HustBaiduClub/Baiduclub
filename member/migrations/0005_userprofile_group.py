# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('member', '0004_auto_20150730_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ForeignKey(to='group.Group', blank=True, null=True),
        ),
    ]
