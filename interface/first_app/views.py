from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def load(request):
    return render(request, 'load.html')

def create(request):
    return render(request, 'create.html')