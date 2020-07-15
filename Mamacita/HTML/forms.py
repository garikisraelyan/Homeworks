from django import forms
from django.forms import ModelForm
from Person.models import Person

class NameForm(ModelForm):
	class Meta:
		model = Person
		fields = ('first_name', 'last_name', 'profile_pic')