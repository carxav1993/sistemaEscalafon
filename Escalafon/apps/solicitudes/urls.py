from django.conf.urls import include, url

urlpatterns = [

	url(r'^$', 'apps.solicitudes.views.inicio', name='inicio'),

]