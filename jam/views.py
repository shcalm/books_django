from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book


def index(requests):
    books = Book.objects.all()
    context = {'book_list':books}
    return render(requests, 'jam/index.html', context)


def book_detail(requests,book_id):
    book = Book.objects.get(doubanid=book_id)
    context={'book':book}
    return render(requests, 'jam/bookdetail.html', context)

def login(requests):
    return render(requests,'jam/login.html')

def register(requests):
    return render(requests,'jam/register.html')

def doregister(requests):
    return