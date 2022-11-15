import openai 
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def generate(request):
    name = request.POST['name']
    response = openai.train(name)
    return HttpResponse(response)
