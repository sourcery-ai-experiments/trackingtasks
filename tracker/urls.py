from django.urls import path
from django.views.generic import TemplateView
from tracker import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='main_page.html'), name="main"),
    path('tasks', views.TaskListView.as_view(), name="task_list"),
]