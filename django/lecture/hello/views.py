from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def dan(request):
    return HttpResponse("Hello, Dan!")

def sarah(request):
    return HttpResponse("Hello, Sarah!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
