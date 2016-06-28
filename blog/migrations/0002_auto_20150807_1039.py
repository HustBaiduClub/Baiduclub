# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='img_url',
            field=models.CharField(max_length=100, blank=True, default='', null=True),
        ),
    ]
