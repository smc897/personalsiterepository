# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
