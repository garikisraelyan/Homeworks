from django.db import models

# Create your models here.

class Albums(models.Model):
	singer_name = models.CharField(max_length=30)
	album_name = models.CharField(max_length=30)
	release_year = models.DateField('date released')

class Songs(models.Model):
	album = models.ForeignKey(Albums, on_delete=models.CASCADE)
	song_name = models.CharField(max_length=30)
	favorite = models.IntegerField(default=0)