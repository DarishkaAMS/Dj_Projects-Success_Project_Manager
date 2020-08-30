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
      "members": task.member.all(),
      "non_member": TeamMember.objects.exclude(task=task).all()
    })

def join(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        member = TeamMember.objects.get(pk = int(request.POST["member"]))
        member.task.add(task)
        return HttpResponseRedirect(reverse("task", args = (task_id,)))