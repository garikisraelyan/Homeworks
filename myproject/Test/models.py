from django.db import models

# Create your models here.
class Avto(models.Model):
	name = models.CharField(max_length=250)
	color = models.CharField(max_length=250)
	year = models.IntegerField()


class User(models.Model):
	name = models.CharField(max_length=250)
	surname = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	password = models.CharField(max_length=250)