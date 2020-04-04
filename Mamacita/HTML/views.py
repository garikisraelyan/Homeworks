from django.shortcuts import render
from datetime import datetime
# Create your views here.
from Form.models import Form

def html_file1(request):
	obj_1 = Form.objects.all()[0]
	dict1 = {
		"Name": obj_1.first_name, 
		"Surname": obj_1.last_name, 
		"From": obj_1.from_adress, 
		"Out": obj_1.out_time, 
		"To": obj_1.to_adress, 
		"Purpose": obj_1.porpose, 
		"Return": obj_1.back_time
		}
	return render(request, 'HTML/file1.html', dict1)

def html_file2(request):
	return render(request, 'HTML/file2.html')
