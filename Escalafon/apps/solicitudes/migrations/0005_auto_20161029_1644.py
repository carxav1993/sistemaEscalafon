# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0004_auto_20161029_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proceso',
            name='id',
        ),
        migrations.AlterField(
            model_name='proceso',
            name='nombre',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
