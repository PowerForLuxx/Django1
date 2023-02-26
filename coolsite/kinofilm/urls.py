from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name=''),
    path('about/',about,name='about'),
]