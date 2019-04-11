from django.db import models


class Product(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=200)
    cena = models.IntegerField(default=0)