from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('Hello Django and Docker')

def hello(request):
    return render(request, 'hello.html')