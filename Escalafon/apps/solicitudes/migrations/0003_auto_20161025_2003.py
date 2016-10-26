# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_evidencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('cedula', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('apellidoNombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('fechaIngresoU', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaInico', models.DateField()),
                ('fechaCierre', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='apellidoNombre',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='email',
        ),
        migrations.RemoveField(
            model_name='inscripcion',
            name='fechaIngresoU',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='docente',
            field=models.ForeignKey(default=0, to='solicitudes.Docente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='proceso',
            field=models.ForeignKey(default=0, to='solicitudes.Proceso'),
            preserve_default=False,
        ),
    ]
