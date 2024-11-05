from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"
    ROLES_CHOICES = (
        (CREATOR, "Créateur"),
        (SUBSCRIBER, "Abonné"),
    )
    profile_photo = models.ImageField(verbose_name="Photo de profil",upload_to='profile/')
    role=models.CharField(max_length=10,choices=ROLES_CHOICES,verbose_name='Rôle')

