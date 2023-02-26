from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = ["О сайте","Добавить фильм","Обратная связь","Войти"]

def index(request):
    posts = Movie.objects.all()
    return render(request,'kinofilm/index.html',{'posts':posts,'menu':menu,'title': 'Main Page'})

def about(request):
    return render(request,'kinofilm/about.html',{'menu':menu,'title': 'About us'})

def categories(request,catid):
    if(request.POST):
     print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year)>2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')