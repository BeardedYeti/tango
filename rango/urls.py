from django.conf.urls import url
from django.conf.urls import url
from django.conf.urls import include
from rango import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', include('about.urls')),
]