from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    return render(request, "contact.html")

def new(request):
    return HttpResponse("New Products:")

