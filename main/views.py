from curses.ascii import HT
from django.shortcuts import render
from .models import Post

title = 'MatrixDisabler'

def home(request):
    context = {
        'title': title,
        'subtitle': 'home'
    }
    return render(request, 'main/home.html', context)

def blog(request):
    context = {
            'posts': Post.objects.all(),
            'title': title,
            'subtitle': 'context'
        }
    return render(request, 'main/blog.html', context)

def about(request):
    context = {
        'title': title,
        'subtitle': 'about'
    }
    return render(request, 'main/about.html', context)
