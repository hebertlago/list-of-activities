from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
# Create your views here.

#def task_list(request):
#    tasks = Task.objects.all()
#    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form
        return super().form_valid(form)
        
    