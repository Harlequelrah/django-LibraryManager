from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def viewbooks(request):
    books=Book.objects.all()
    return render(request,'books/viewbooks.html',{'books':books})
def about(request):
    return HttpResponse("<h1> Contactez nous </h1>"
    )
