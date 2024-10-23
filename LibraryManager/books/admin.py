from django.contrib import admin

# Register your models here.
from .models import Book,Genre
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'stars','is_available')

class AdminGenre(admin.ModelAdmin):
    list_display = ('name','description')
admin.site.register(Book,AdminBook)
admin.site.register(Genre, AdminGenre)
