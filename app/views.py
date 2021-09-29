from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def enter(request):
    return render(request,'enter.html')

def judging(request):
    return render(request,'judging.html')

def media(request):
    return render(request,'media-centre.html')

def contact(request):
    return render(request,'contact-us.html')

def awards(request):
    return render(request,'awards.html')

def vote(request):
    return render(request,'vote-now.html')