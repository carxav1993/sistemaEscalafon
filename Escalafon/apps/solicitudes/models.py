from django.db import models

# Create your models here.

class inscripcion(models.model):
	cedula = models.Charfield(max_length=10)
	apellidoNombre = models.Charfield(max_length=150)
	