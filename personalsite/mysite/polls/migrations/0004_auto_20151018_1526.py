# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
