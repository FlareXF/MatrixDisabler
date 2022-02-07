from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')
# Create your views here.
