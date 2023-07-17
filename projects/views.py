from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def project(request):
    projects = Project.objects.all()
    return render(request,"project.html", {'projects': projects})

def new(request):
    return HttpResponse("New Products:")

