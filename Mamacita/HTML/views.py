from django.shortcuts import render
from datetime import datetime
# Create your views here.
from Form.models import Form
from Person.models import Person
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm

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


# def find_pers(request, person_id):
# 	obj = Person.objects.get(pk=person_id)
# 	dict2 = {
# 		'Name': obj.first_name,
# 		'Surname': obj.last_name,
# 		'Image': obj.image,
# 	}
# 	return render(request, 'HTML/file_pers.html', dict2)


def new_find(request, person_id):
	obj_2 = Person.objects.get(pk=person_id)
	context = {'person_info': obj_2}
	return render(request, 'HTML/new_file.html', context)


def find_name(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		# print(request.POST['your_name'])

		if form.is_valid():
			return HttpResponseRedirect('/Person/my_name')
	else:
		form = NameForm()

	return render(request, 'HTML/forms.html', {'form': form})

# def go_to(request):
# 	return HttpResponse('hi')