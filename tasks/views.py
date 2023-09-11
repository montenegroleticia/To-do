from django.shortcuts import render
from django.http import HttpResponse

def health(request):
    return HttpResponse("I'm alive!")

def taskList(request):
    return render(request, 'tasks/list.html')

