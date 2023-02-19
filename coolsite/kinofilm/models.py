from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=32)


class Movie(models.Model):
    Name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    Description = models.TextField(blank=True)
    Price = models.IntegerField
    Place = models.IntegerField

