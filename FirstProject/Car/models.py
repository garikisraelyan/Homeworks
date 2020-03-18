from django.db import models

# Create your models here.

class Car(models.Model):
    production_year = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    mark = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    number_of_doors = models.CharField(max_length=30)
    hp = models.CharField(max_length=30)