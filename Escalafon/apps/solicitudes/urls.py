from django.conf.urls import include, url

urlpatterns = [

	url(r'^$', 'apps.solicitudes.views.inicio', name='inicio'),


	#llamadasAjax
	url(r'^traerCarreras/$','apps.solicitudes.views.traerCarreras', name='traer_carreras'),
	url(r'^anadirPersonal_traerArchivos/$','apps.solicitudes.views.anadirPersonalTraerArchivos', 
		name='anadirPersonal_traerArchivos'),
]