from django.shortcuts import render
from django.views.generic import ListView
from .models import Task
# Create your views here.

#def task_list(request):
#    tasks = Task.objects.all()
#    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
