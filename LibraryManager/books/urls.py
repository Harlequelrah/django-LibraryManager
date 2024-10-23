from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    path("", viewbooks,name='book-list'),
    path('<int:book_id>/',viewbook,name='book-detail')
]
