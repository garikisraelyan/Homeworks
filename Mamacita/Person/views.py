from django.shortcuts import render
# Create your views here.
from .models import Person
from django.http import HttpResponse

def my_name(request):
	obj = Person.objects.all()
	response_list = []
	for i in obj:
		response_list.append(i.first_name + " " + i.last_name + '<br>')

	return HttpResponse(''.join(response_list))