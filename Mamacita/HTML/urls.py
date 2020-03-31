from django.urls import path
from . import views

urlpatterns = [
	path('', views.html_file1),
	path('', views.html_file2),
]
