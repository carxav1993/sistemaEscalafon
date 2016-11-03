from django.conf.urls import include, url

urlpatterns = [

	url(r'^$', 'apps.solicitudes.views.inicio', name='inicio'),
	url(r'^inscripcionExitosa/$','apps.solicitudes.views.inscripcionExitosa', name='inscripcion_exitosa'),


	#llamadasAjax
	url(r'^traerCarreras/$','apps.solicitudes.views.traerCarreras', name='traer_carreras'),
	url(r'^anadirPersonal/$','apps.solicitudes.views.anadirPersonal', name='anadir_personal'),
	url(r'^traerRequisitos/$','apps.solicitudes.views.traerRequisitos', name='traer_requisitos'),
]