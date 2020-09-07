from django import forms
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, "projects/index.html", {
        "projects": Task.objects.all()  
    })