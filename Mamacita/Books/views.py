from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Books

def show_books(request):
	response_list = []
	obj_1 = Books.objects.filter(name="Book")
	return HttpResponse(obj_1.order_by('publishing_date'))