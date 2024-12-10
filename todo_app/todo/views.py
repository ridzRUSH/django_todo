from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('list_tasks')
    return render(request, 'tasks/add_task.html')

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})
