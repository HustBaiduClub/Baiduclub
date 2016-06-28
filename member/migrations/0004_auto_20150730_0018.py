# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20150729_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='portrait',
            field=models.ImageField(upload_to='img'),
        ),
    ]
