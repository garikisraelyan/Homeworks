from django.db import models

# Create your models here.
class Form(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	from_adress = models.CharField(max_length=30)
	out_time = models.DateTimeField('out time')
	to_adress = models.CharField(max_length=30)
	porpose = models.CharField(max_length=50)
	back_time = models.DateTimeField('return time')