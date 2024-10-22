from django.contrib import admin

# Register your models here.
from .models import Book
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author','label', 'published_year', 'cover_image')
admin.site.register(Book,AdminBook)
