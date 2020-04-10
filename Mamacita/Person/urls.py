from django.urls import path
from . import views

urlpatterns = [
	path('my_name', views.my_name)
]