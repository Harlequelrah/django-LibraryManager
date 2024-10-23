from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def viewbooks(request):
    books=Book.objects.all()
    return render(request,'books/book_list.html',{'books':books})


def viewbook(request,book_id):
    book=Book.objects.get(id=book_id)
    stars = "✨" * book.stars
    return render(request,'books/book_detail.html',{'book':book,'stars':stars})
