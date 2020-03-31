from django.shortcuts import render
from datetime import datetime
# Create your views here.
from Car.models import Car

def html_file1(request):
	obj_1 = Car.objects.all()[0]
	dict1 = {"Mark": obj_1.mark, "Price": obj_1.price}
	return render(request, 'HTML/file1.html', dict1)

def html_file2(request):
	return render(request, 'HTML/file2.html', )