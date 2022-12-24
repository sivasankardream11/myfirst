from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def anil(request):
    return HttpResponse('<marquee>hello t.anil</marquee>')
def manju(request):
    return HttpResponse('<h1> hi manju</h1>')