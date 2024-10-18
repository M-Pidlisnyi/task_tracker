from django.urls import path

from .views import TaskListView, TaskDetailView,TaskCreateView

urlpatterns = [
    path("list/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>" ,TaskDetailView.as_view(),name="task-detail"),
    path("task/new/",TaskCreateView.as_view(),name="create-task")
]
