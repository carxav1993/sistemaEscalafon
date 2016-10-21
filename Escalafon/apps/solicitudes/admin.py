from django.contrib import admin
from .models import UnidadAcademica, Carrera, Categoria, Requisito, Inscripcion, InscripcionRequisito

# Register your models here.
admin.site.register(UnidadAcademica)
admin.site.register(Carrera)
admin.site.register(Categoria)
admin.site.register(Requisito)
admin.site.register(Inscripcion)
admin.site.register(InscripcionRequisito)