from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<br/> <a href="/rango/about/">About</a>Rango says hey partner!')


def about(request):
    return HttpResponse('<a href="/rango/">Home</a>Rango says here is the about page.')
