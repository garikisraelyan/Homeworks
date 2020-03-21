from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Car

def index(request):
	obj_1 = Car.objects.all()
	response_list = []
	for i in obj_1:
		response_list.append(i.owner_name + "   " + i.mark + "<br>")
	return HttpResponse(''.join(response_list))