from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def sai(request):
    return HttpResponse('<h1>hello sai</h1>')
def jai(request):
    return HttpResponse('<h2><i>hello jai</i></h2>')