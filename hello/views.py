from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def aishwary(request):
    return HttpResponse("Namaste, Aishwary J")

def first(request):
    return HttpResponse("first")

def second(request):
    return HttpResponse("second")

def third(request):
    return HttpResponse("third")

def next(request):
    return HttpResponse("next")

#def greetold(request, name):
#    return HttpResponse (f"hello {name.capitalize()}")

def greet(request, name):
    return render (request, "hello/greet.html",{
        "name":name.capitalize()
    })
