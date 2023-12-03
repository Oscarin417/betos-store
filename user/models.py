from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    imagen = models.ImageField(upload_to='profiles/', null=True, blank=True)