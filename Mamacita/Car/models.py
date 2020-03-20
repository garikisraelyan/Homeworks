from django.db import models

# Create your models here.
class Car(models.Model):
    production_year = models.IntegerField()
    price = models.IntegerField()
    mark = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    hp = models.IntegerField()
    number_of_doors = models.IntegerField()