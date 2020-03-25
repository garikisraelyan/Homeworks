from django.shortcuts import render
from .models import Question, Choice
from django.http import HttpResponse
# Create your views here.

def detail(request, question_id):
	question = Question.objects.get(pk=question_id)
	response_list = []
	choices = Choice.objects.filter(question=question_id)
	for i in choices:
		response_list.append('<br>' + i.choice_text + " " + str(i.votes))
	return HttpResponse(question.question_text + ''.join(response_list))