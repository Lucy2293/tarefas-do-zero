from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
# Create your views here.

def update (request, task_id) :
    return JsonResponse ({'error' : 'Invalid data'} , status=400)
def listar(request) :
    if request.method == "GET" :
        tasks = Task.objects.all()
        return render(request, 'index.html' , {'tasks' : tasks})
    