from django.db import models

# Create your models here.

from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=255,blank=True,null=True)
    doubanid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_intro = models.TextField()
    publisher = models.CharField(max_length=255)
    date = models.DateField()
    rate = models.FloatField()
    ratenumber = models.IntegerField()
    tags = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    imgs = models.CharField(max_length= 255)
    summary = models.TextField()
    catalog = models.TextField()
    pages = models.IntegerField()
    downloadnum = models.IntegerField(default=0,null=True,blank=True)
    filelocation = models.CharField(max_length=255,default='',blank=True,null=True)
    filename = models.CharField(max_length=255)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    book_number = models.IntegerField(default=0,null=True,blank=True)
