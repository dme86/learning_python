from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")      # see templates/hello

def dan(request):
    return HttpResponse("Hello, Dan!")

def sarah(request):
    return HttpResponse("Hello, Sarah!")

def greet(request, name):
    return render(request, "hello/greet.html", {
            "name": name.capitalize()               # dictionary context as variable name for template
        })
