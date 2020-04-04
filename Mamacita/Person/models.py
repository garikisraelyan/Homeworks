from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	profile_pic = models.ImageField(upload_to='media/', null=True, blank=True)