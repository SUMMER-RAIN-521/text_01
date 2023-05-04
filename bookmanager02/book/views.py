from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("hello,平凡")
