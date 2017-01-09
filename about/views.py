from django.shortcuts import render

from django.http import HttpResponse

def about(request):
	return HttpResponse("About says hey there partner! <br/> <a href='/rango/'>Index</a>")