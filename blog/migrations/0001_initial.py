# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=80)),
                ('photo', models.ImageField(null=True, verbose_name='上传图片', blank=True, upload_to='img')),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('user', models.CharField(max_length=254)),
                ('img_url', models.CharField(null=True, default='', max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('blog', models.ForeignKey(to='blog.Post')),
            ],
        ),
    ]
