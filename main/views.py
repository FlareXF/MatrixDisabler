from curses.ascii import HT
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

title = 'Gatka'

def home(request):
    context = {
        'title': title,
        'subtitle': 'home',
        'name': cut_name(request)
    }
    return render(request, 'main/home.html', context)

def blog(request):
    context = {
            'posts': Post.objects.all(),
            'title': title,
            'subtitle': 'context',
            'name': cut_name(request)
        }
    return render(request, 'main/blog.html', context)

def about(request):
    context = {
        'title': title,
        'subtitle': 'about',
        'name': cut_name(request)

    }
    return render(request, 'main/about.html', context)


def cut_name(request):
    nameuser = request.user.username
    if len(nameuser) > 10:
        return (nameuser[:8] + '..')