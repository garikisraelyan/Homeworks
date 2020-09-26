from django.shortcuts import render
from .models import Avto
from .forms import AvtoForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
	obj = Avto.objects.all()
	context = {"cars": obj}
	return render(request, 'Test/index.html', context)

def register(request):
	if request.method == 'POST':
		form = AvtoForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = AvtoForm()

	return render(request, 'Test/register.html', {'form': form})



def thanks(request):
	return render(request, 'Test/thanks.html')


def sign_up(request):
	if request.method == 'POST':
		form = UserForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = UserForm

	return render(request, 'Test/sign_up.html', {'form': form})