#encoding:utf-8
from django.db import models

# Create your models here.

class UnidadAcademica(models.Model):
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		return self.nombre

class Carrera(models.Model):
	nombre = models.CharField(max_length=100)
	unidadAcademica = models.ForeignKey(UnidadAcademica)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

class Requisito(models.Model):
	nombre = models.CharField(max_length=500)
	categoria = models.ForeignKey(Categoria)

	def __unicode__(self):
		return "%s %s" % (self.categoria.nombre, self.nombre)

class Evidencia(models.Model):
	requisito = models.ForeignKey(Requisito)
	nombre = models.CharField(max_length=500)

	def __unicode__(self):
		return "%s %s %s" % (self.requisito.categoria.nombre, self.requisito.nombre, self.nombre)

class Docente(models.Model):
	cedula = models.CharField(primary_key=True, max_length=10)
	apellidoNombre = models.CharField(max_length=150)
	email = models.EmailField()
	fechaIngresoU = models.DateTimeField()

	def __unicode__(self):
		return "%s %s" % (self.cedula, self.apellidoNombre, self.email)

class Proceso(models.Model):
	nombre = models.CharField(max_length=100)
	fechaInico = models.DateField()
	fechaCierre = models.DateField()

	def __unicode__(self):
		return "%s %s %s" % (self.nombre, self.fechaInico, self.fechaCierre)

class Inscripcion(models.Model):	
	docente = models.ForeignKey(Docente)
	proceso = models.ForeignKey(Proceso)
	carrera = models.ForeignKey(Carrera)
	categoriaActual = models.ForeignKey(Categoria, related_name='categoriaActual')
	categoriaSolicitada = models.ForeignKey(Categoria, related_name='categoriaSolicitada')
	fechaInscripcion = models.DateTimeField()
	fechaEvaluacion = models.DateTimeField()
	aprobacion = models.BooleanField()

	def __unicode__(self):
		return "%s %s %s" % (self.cedula, self.apellidoNombre, self.carrera.nombre)

class InscripcionRequisito(models.Model):
	inscripcion = models.ForeignKey(Inscripcion)
	requisito = models.ForeignKey(Requisito)
	archivo = models.FileField(upload_to='solicitudes/pdf')
	cumple = models.BooleanField()
	observacion = models.CharField(max_length=500)

	def __unicode__(self):
		return "%s %s %s" %(self.inscripcion.apellidoNombre, self.requisito.nombre)
