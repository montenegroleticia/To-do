from django.shortcuts import render
from django.http import HttpResponse

def tasks(request):
    return HttpResponse("I'm alive!")
