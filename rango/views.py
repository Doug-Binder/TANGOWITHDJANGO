from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango Says Hello World!")

def about(request):
	return HttpResponse("RANGO SAYS: ABOUT!!! wat wat")