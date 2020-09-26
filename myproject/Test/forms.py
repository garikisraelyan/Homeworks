from django.forms import ModelForm
from .models import Avto, User

class AvtoForm(ModelForm):
	class Meta:
		model = Avto
		fields = '__all__'


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'