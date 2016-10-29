# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_auto_20161025_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='aprobacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='fechaEvaluacion',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='inscripcionrequisito',
            name='cumple',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inscripcionrequisito',
            name='observacion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
