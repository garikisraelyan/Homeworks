from django.urls import path
from . import views

urlpatterns = [
	path('', views.html_file1),
	path('file2', views.html_file2)
]