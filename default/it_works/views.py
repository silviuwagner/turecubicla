from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("It works! (served from Django)")