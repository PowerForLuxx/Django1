from django.db import models
from django.urls import reverse

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.username


class Movie(models.Model):
    Name = models.CharField(max_length=20, verbose_name="Название")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    Description = models.TextField(blank=True,verbose_name=" Описание")
    Price = models.IntegerField
    Place = models.IntegerField

    def get_absolute_url(self):
        return reverse('post', kwargs ={'post_id':self.pk})

    class Meta:
        verbose_name = 'Известные фильмы'
        verbose_name_plural = 'Известные фильмы'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


