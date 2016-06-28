# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('group_img', models.ImageField(upload_to='img')),
                ('group', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=200)),
            ],
        ),
    ]
