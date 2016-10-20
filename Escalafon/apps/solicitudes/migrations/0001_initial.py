# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=10)),
                ('apellidoNombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('fechaIngresoU', models.DateTimeField()),
                ('fechaInscripcion', models.DateTimeField()),
                ('fechaEvaluacion', models.DateTimeField()),
                ('aprobacion', models.BooleanField()),
                ('carrera', models.ForeignKey(to='solicitudes.Carrera')),
                ('categoriaActual', models.ForeignKey(related_name='categoriaActual', to='solicitudes.Categoria')),
                ('categoriaSolicitada', models.ForeignKey(related_name='categoriaSolicitada', to='solicitudes.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='InscripcionRequisito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to=b'solicitudes/pdf')),
                ('cumple', models.BooleanField()),
                ('observacion', models.CharField(max_length=500)),
                ('inscripcion', models.ForeignKey(to='solicitudes.Inscripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('categoria', models.ForeignKey(to='solicitudes.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='inscripcionrequisito',
            name='requisito',
            field=models.ForeignKey(to='solicitudes.Requisito'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='unidadAcademica',
            field=models.ForeignKey(to='solicitudes.UnidadAcademica'),
        ),
    ]
