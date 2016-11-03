# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_auto_20161029_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='fechaInscripcion',
            field=models.DateTimeField(null=True),
        ),
    ]
