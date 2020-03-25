from django.shortcuts import render
from .models import Albums, Songs
from django.http import HttpResponse
# Create your views here.

def show_info(request, album_id):
	response_list = []
	my_albums = Albums.objects.get(pk=album_id)
	my_songs = Songs.objects.filter(album=album_id)
	for i in my_songs:
		response_list.append('<br>' + i.song_name + " " + str(i.favorite))
	return HttpResponse(my_albums.album_name + " " + ''.join(response_list))