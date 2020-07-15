from django.db import models
import datetime

# Create your models here.

def year_choices():
	return [(r,r) for r in range(1984, datetime.date.today().year+1)]

CAR_MODELS = (
	(1, "BMW"),
	(2, "Mercedes-Benz"),
	(3, "Nissan"),
	(4, "Toyota"),
	(5, "Mazda")
	)

class Car(models.Model):
	mark = models.IntegerField(choices=CAR_MODELS)
	model = models.CharField(max_length=200)
	year = models.IntegerField(choices=year_choices())
	price = models.IntegerField()
	photo = models.ImageField(upload_to='media', null=True, blank=True)