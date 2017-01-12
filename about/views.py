from django.shortcuts import render

from django.http import HttpResponse

def about(request):
	context_dict = {'Pickles': "Kitty no like pickles!"}

	return render(request, 'about/about.html', context=context_dict)