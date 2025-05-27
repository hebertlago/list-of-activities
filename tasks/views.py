from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        queryset = super().get_queryset()
        status_filter = self.request.GET.get('status', '')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form
        return super().form_valid(form)
        
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')
    
    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form
        return super().form_valid(form)