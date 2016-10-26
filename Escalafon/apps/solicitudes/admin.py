from django.contrib import admin
from .models import UnidadAcademica, Carrera, Categoria, Requisito, Evidencia, Inscripcion, InscripcionRequisito, Proceso, Docente

# Register your models here.
admin.site.register(UnidadAcademica)
admin.site.register(Carrera)
admin.site.register(Categoria)
admin.site.register(Requisito)
admin.site.register(Evidencia)
admin.site.register(Inscripcion)
admin.site.register(InscripcionRequisito)
admin.site.register(Proceso)
admin.site.register(Docente)