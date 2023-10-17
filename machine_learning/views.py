from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myFunc(response):
    return HttpResponse("This is a test project")