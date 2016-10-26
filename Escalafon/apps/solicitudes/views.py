#encoding:utf-8
from django.shortcuts import render, redirect
from .models import UnidadAcademica, Carrera, Categoria, Requisito, Evidencia, Inscripcion, InscripcionRequisito, Docente, Proceso
from django.http import JsonResponse, HttpResponse
from django.core import serializers
# Create your views here.
def inicio(request):
	categorias = Categoria.objects.all()
	unidadesAcademicas = UnidadAcademica.objects.all()
	return render(request, 'solicitudes/index.html',{'categorias':categorias, 'unidadesAcademicas':unidadesAcademicas})



#vistas de ajax
def traerCarreras(request):
	if request.is_ajax():
		idUnidadAcademica = request.GET['codigo']
		print "Recibe la id "+idUnidadAcademica
		ua = UnidadAcademica.objects.get(id=idUnidadAcademica)
		print ua
		carreras = Carrera.objects.filter(unidadAcademica_id=idUnidadAcademica)
		print carreras
		#list_carreras = list(carreras)
		#print list_carreras
		#return JsonResponse(list_carreras, safe=False)
		carreras = serializers.serialize('json', carreras)
		print carreras
		return HttpResponse(carreras, content_type="application/json")
	else:
		return redirect ('/')

def anadirPersonalTraerArchivos(request):
	if request.is_ajax():
		cedula = request.GET['cedula']
		if Docente.objects.filter(cedula=cedula).count() == 0:
			apellidoNombre = request.GET['apellidos'] + " " + request.GET['nombres']
			email = request.GET['email']
			fi = request.GET['fi']

			docente = Docente()
			docente.cedula = cedula
			docente.apellidoNombre = apellidoNombre
			docente.email = email
			docente.fechaIngresoU = fi
			docente.save()

		ua = request.GET['ua']
		carrera = request.GET['carrera']
		cac = request.GET['cac']
		cas = request.GET['cas']
		fs = request.GET['fs']

		inscripcion = Inscripcion()
		inscripcion.docente = cedula
		inscripcion.proceso = "PE-0001"
		inscripcion.carrera = carrera
		inscripcion.categoriaActual = cac
		inscripcion.categoriaSolicitada = cas
		inscripcion.fechaSolicitud = fs
		inscripcion.save()
		

		# print apellidoNombre +" "+cedula+ " "+email+" "+ua+" "+carrera+" "+ua+" "+carrera+" "+cac+" "+cas+" "+fi+" "+fs 

		requisitos = Requisito.objects.filter(categoria=cas)
		print requisitos
		requisitos = serializers.serialize('json',requisitos)
		print requisitos

		return HttpResponse(requisitos, content_type="application/json")

	else:
		return ('/')