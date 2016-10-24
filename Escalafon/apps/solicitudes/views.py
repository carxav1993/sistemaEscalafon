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

