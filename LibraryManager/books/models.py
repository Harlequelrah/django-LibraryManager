from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Book(models.Model):
    title=models.CharField(verbose_name='titre',max_length=150)
    description=models.CharField(verbose_name='description',max_length=100)
    author=models.CharField(max_length=150,verbose_name='auteur')
    published_date=models.DateTimeField(verbose_name='année de publication')
    cover_image=models.ImageField(verbose_name='couverture',null=True,blank=True)
    available=models.BooleanField(verbose_name='disponibilité',default=True)
    stars=models.IntegerField(default=0,validators=[
        MinValueValidator(0)
    ])
    genre=models.ManyToManyField('Genre',related_name='books')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name=models.fields.CharField(verbose_name='nom',max_length=50)
    description=models.fields.CharField(max_length=100)
    def __str__(self):
        return self.name


