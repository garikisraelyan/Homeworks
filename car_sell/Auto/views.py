from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from .form import CarForm
from .models import Car

def add_car(request):
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('create/')

	else:
		form = CarForm()

	return render(request, 'Auto/index.html', {'form': form})

def view_cars(request):
	return HttpResponse(Car.objects.all())