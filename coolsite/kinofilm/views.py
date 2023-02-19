from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def index(request):
    return HttpResponse("Страница приложения")

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