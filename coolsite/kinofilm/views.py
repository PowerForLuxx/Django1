from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить Фильм", 'url_name': 'add_page'},
        {'title': "Обратная Связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request):
    posts = Movie.objects.all()
    context = {
        'posts' : posts,
        'menu' : menu,
        'title' : 'Главная страница'
    }
    return render(request,'kinofilm/index.html',context=context)

def about(request):
    return render(request,'kinofilm/about.html',{'menu':menu,'title': 'О сайте'})

def addpage(request):
    return  HttpResponse("Добавление фильма")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request,post_id):
    return HttpResponse(f"Фильм с айди = {post_id}")
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')