from django.shortcuts import render
from .models import Movie

# Create your views here.
def movies(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies.html', context)

def hello_world(request):
    name = request.GET.get('name')
    context = {
        'name': name
    }
    return render(request, "hello.html", context)

def hello_name(request, name):
    context = {
        'name': name
    }
    return render(request, "hello.html", context)

def hello2(request, name=None):
    if name == None:
        name = request.GET.get('name')

    return render(request, "hello.html", {'name': name })