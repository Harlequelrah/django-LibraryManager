from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.fields.CharField(verbose_name='titre',max_length=150)
    label=models.fields.CharField(verbose_name='description',max_length=100)
    author=models.fields.CharField(max_length=150,verbose_name='auteur')
    publication_date=models.fields.DateTimeField(verbose_name='année de publication')
    cover_image=models.ImageField(verbose_name='couverture',null=True)
    available=models.fields.BooleanField(verbose_name='disponibilité',default=True)
    stars=models.fields.IntegerField(default=0)
    genre=models.ForeignKey('Genre',on_delete=models.SET_DEFAULT,default='UNKNOW',related_name='genres')

    def __str__(self):
        return self.title


class Genre(models.Model):
    name=models.fields.CharField(verbose_name='nom',max_length=50)
    description=models.fields.CharField(max_length=100)
    def __str__(self):
        return self.name


