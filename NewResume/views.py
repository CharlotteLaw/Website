from django.shortcuts import render
from django.http import HttpResponse


def newresume(request):
    return render(request,"newresume.html")

def new(request):
    return HttpResponse("New Products:")

