from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'movies': ['Batman Begin', 'Batman Dark Knight', 'Batman Forever']
    }
    return render(request, 'movies/index.html', context)

# "app"/template/"app"/index.html => movies/templates/movies/index.html

def about(request):
    return render(request, 'movies/about.html', {})

