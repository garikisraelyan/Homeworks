from django.urls import path
from . import views
urlpatterns = [
	path('create', views.add_car),
	path('thanks', views.view_cars),
]