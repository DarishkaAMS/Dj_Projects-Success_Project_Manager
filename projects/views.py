from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Task, TeamMember

def index(request):
    return render(request, "projects/index.html", {
        "projects": Task.objects.all()  
    })

def task(request, task_id):
    task = Task.objects.get(pk = task_id)
    return render(request,"projects/task.html", {
      "task": task,
      "members": task.member.all()
    })

