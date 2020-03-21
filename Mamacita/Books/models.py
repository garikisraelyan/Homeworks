from django.db import models

# Create your models here.
class Books(models.Model):
	name = models.CharField(max_length=50)
	publishing_date = models.CharField(max_length=8)
	author_name = models.CharField(max_length=30)
	publisher = models.CharField(max_length=30)