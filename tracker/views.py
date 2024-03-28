from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from tracker.models import Task
from tracker.forms import TaskForm

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tracker/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tracker/task_detail.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'tracker/task_form.html'
    form_class = TaskForm
    success_url = reverse_lazy("task_list")
