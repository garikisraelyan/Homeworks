from django.forms import ModelForm, ImageField
from .models import Car

class CarForm(ModelForm):
	class Meta:
		model = Car
		fields = '__all__'