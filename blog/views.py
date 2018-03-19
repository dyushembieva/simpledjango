from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = ['python', 'html', 'css', 'django']
    return render(request, 'blog/index.html', {'saikal': a})

def generic(request):
    return render(request, 'blog/generic.html', {})

