from django.db import models

# Create your models here.

class Per(models.Model):
    Personaje = models.CharField(max_length=50)
    Saga = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
