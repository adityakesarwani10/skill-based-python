from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def test(request):
    return HttpResponse("This is the test page.")

def show(request):
    return HttpResponse("Now we have understand the concept of url mapping...")
