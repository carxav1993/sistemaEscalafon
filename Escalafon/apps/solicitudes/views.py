#encoding:utf-8
from django.shortcuts import render, redirect
from .models import UnidadAcademica, Carrera, Categoria, Requisito, Evidencia, Inscripcion, InscripcionRequisito, Docente, Proceso
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import time
# Create your views here.
def inicio(request):
	if request.method == 'POST':
		cedula = request.POST.get('txtCedula')
		if Docente.objects.filter(cedula=cedula).count() == 0:
			docente = Docente()
			docente.cedula = request.POST.get('txtCedula')
			docente.apellidoNombre = '%s %s' %(request.POST.get('txtApellidos'), request.POST.get('txtNombres'))
			docente.email = request.POST.get('txtEmail')
			docente.fechaIngresoU = request.POST.get('txtFechaIngresoU')
			docente.save()
		
		inscripcion = Inscripcion()
		inscripcion.docente = Docente.objects.get(cedula=cedula)
		inscripcion.proceso = "PE-0001"
		inscripcion.carrera = request.POST.get('ddCarreras')
		inscripcion.categoriaActual = request.POST.get('ddCategoriaActual')
		inscripcion.categoriaSolicitada = request.POST.get('ddCategoriaAspirada')
		print time.strftime("%x")
		inscripcion.fechaSolicitud = time.strftime("%x")
		inscripcion.save()

		idInscripcion = inscripcion.id
		print idInscripcion
		
		requisitos = Requisito.objects.filter(categoria_id=request.POST.get('ddCategoriaAspirada'))

		inscripcionRequisito = InscripcionRequisito()
		
		for r in len(requisitos):
			inscripcionRequisito.inscripcion = idInscripcion
			inscripcionRequisito.requisito = requisitos[i].id
			inscripcionRequisito.archivo = request.POST.get('archi'+r)
			inscripcionRequisito.save()
		return redirect('/')
	else:
		categorias = Categoria.objects.all().order_by('nombre')
		unidadesAcademicas = UnidadAcademica.objects.all()
		return render(request, 'solicitudes/index.html',{'categorias':categorias, 'unidadesAcademicas':unidadesAcademicas})


#vistas de ajax
def traerCarreras(request):
	if request.is_ajax():
		idUnidadAcademica = request.GET['codigo']
		print "Recibe la id "+idUnidadAcademica
		ua = UnidadAcademica.objects.get(id=idUnidadAcademica)
		print ua
		carreras = Carrera.objects.filter(unidadAcademica_id=idUnidadAcademica).order_by('nombre')
		print carreras
		carreras = serializers.serialize('json', carreras)
		print carreras
		return HttpResponse(carreras, content_type="application/json")
	else:
		return redirect ('/')

def traerRequisitos(request):
	if request.is_ajax():
		idRequisito = request.GET['id']
		print "Id del requisito: " + idRequisito
		requisitos = Requisito.objects.filter(categoria_id=idRequisito)
		print requisitos
		requisitos = serializers.serialize('json', requisitos)
		print requisitos
		return HttpResponse(requisitos, content_type="application/json")
	else:
		return redirect('/')

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