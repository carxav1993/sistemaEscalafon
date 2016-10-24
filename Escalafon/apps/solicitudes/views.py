#encoding:utf-8
from django.shortcuts import render, redirect
from .models import UnidadAcademica, Carrera, Categoria, Requisito, Evidencia, Inscripcion, InscripcionRequisito
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
		apellidoNombre = request.GET['apellidos'] + " " + request.GET['nombres']
		cedula = request.GET['cedula']
		email = request.GET['email']
		ua = request.GET['ua']
		carrera = request.GET['carrera']
		cac = request.GET['cac']
		cas = request.GET['cas']
		fi = request.GET['fi']
		fs = request.GET['fs']

		print apellidoNombre +" "+cedula+ " "+email+" "+ua+" "+carrera+" "+ua+" "+carrera+" "+cac+" "+cas+" "+fi+" "+fs 

		# inscripcion = Inscripcion()
		# inscripcion.apellidoNombre = apellidoNombre
		# inscripcion.cedula = cedula
		# inscripcion.email = email
		# inscripcion.carrera = carrera
		# inscripcion.categoriaActual = cac
		# inscripcion.categoriaSolicitada = cas
		# inscripcion.fechaIngresoU = fi
		# inscripcion.fechaInscripcion = fs
		
		# inscripcion.save()

		requisitos = Requisito.objects.filter(categoria=cas)
		print requisitos
		requisitos = serializers.serialize('json',requisitos)
		print requisitos

		return HttpResponse(requisitos, content_type="application/json")

	else:
		return ('/')