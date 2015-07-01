# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactmgr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
