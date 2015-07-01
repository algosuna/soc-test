# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b"Contact's full name.", max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=100, blank=True)),
                ('address2', models.CharField(max_length=80, blank=True)),
                ('city', models.CharField(max_length=35, blank=True)),
                ('postal_code', models.CharField(max_length=10, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
