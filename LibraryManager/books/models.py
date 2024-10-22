from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.fields.CharField(verbose_name='titre',max_length=150)
    label=models.fields.CharField(verbose_name='description',max_length=100)
    author=models.fields.CharField(max_length=150,verbose_name='auteur')
    published_year=models.fields.IntegerField(verbose_name='année de publication')
    cover_image=models.ImageField(verbose_name='couverture')




