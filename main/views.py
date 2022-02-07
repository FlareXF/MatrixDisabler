from curses.ascii import HT
from django.shortcuts import render

title = 'MatrixDisabler'

posts = [
    {
        'author': 'Gay',
        'title': 'Post 1',
        'content': 'Ya sosu huy',
        'date_posted': '06/02/2022'
    },
        {
        'author': 'Not gay',
        'title': 'Post 2',
        'content': 'Ya ne sosu huy',
        'date_posted': '07/02/2022'
    }
]

def home(request):
    context = {
        'title': title,
        'subtitle': 'home'
    }
    return render(request, 'main/home.html', context)

def blog(request):
    context = {
            'posts': posts,
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
