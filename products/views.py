from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(request, 'This page is about products')

def root_index(request):
    return HttpResponse(request, 'This is MAIN page')