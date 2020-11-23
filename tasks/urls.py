from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getTasks", views.get_tasks, name="Tasks"),
    path("postTask", views.post_task, name="postTasks"),
    path("deleteTasks", views.delete_tasks, name="deleteTasks"),
]
