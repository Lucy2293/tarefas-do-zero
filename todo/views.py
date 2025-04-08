from django.shortcuts import render
from django.http import JsonResponse
from .models import Task
import json
# Create your views here.

def update (request, task_id) :
    return JsonResponse ({'error' : 'Invalid data'} , status=400)


def listar(request) :
    if request.method == "GET" :
        tasks = Task.objects.all()
        return render(request, 'index.html' , {'tasks' : tasks}) 
    if request.method == "POST":
        data = json.loads(request.body)
        form = TaskForm(data)
        if form.is_valid():
            task = form.save()
            return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed}, status=201)
        return JsonResponse({'error': 'Invalid data'}, status=400)
