from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('register/', views.register),
	path('sign_up/thanks/', views.thanks),
	path('sign_up/', views.sign_up)
]