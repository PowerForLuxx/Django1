from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView
from .forms import *
from .models import *
from .urls import *
from .utils import *


class MovieHome(DataMixin,ListView):
    model = Movie
    template_name =  'kinofilm/index.html'
    context_object_name = 'posts'

    def get_context_data(self, * , object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))

class MovieCategory(ListView):
    model = Movie
    template_name = 'movie/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Movie.objects.filter(cal__slub=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context =super().get_context_data(**kwargs)
        context ['title'] = 'Категория - '+ str(context['posts'[0].cat])
        context['cat_selected'] = context['posts'][0].cat_id
        return context
#def index(request):
#    posts = Movie.objects.all()
#    context = {
#        'posts' : posts,
#        'menu' : menu,
#        'title' : 'Главная страница'
#    }
#    return render(request,'kinofilm/index.html',context=context)

def about(request):
    return "Сведенье"

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'kinofilm/addpage.html'
def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

class ShowPost(DetailView):
    model = Movie
    template_name = 'kinofilm/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context =super().get_context_data(**kwargs)
        context ['title'] = context['post']
        return context

#def show_post(request,post_slug):
#    post = get_object_or_404(Movie,slug = post_slug)
#
#    context = {
#        'post' : post,
#        'menu' : menu,
#        'title': post.title,
#        'cat_selected': post.cat.id,
#    }
#   return render(request, 'movie/post.html', context=context)

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')