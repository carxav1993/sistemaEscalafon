# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0006_auto_20161030_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='fechaIngresoU',
            field=models.DateTimeField(null=True),
        ),
    ]
