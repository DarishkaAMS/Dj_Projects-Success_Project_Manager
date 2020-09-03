from django.urls import path 

from . import views 

from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>", views.task, name="task"),
    path("<int:task_id>/join", views.join, name="join"),
]