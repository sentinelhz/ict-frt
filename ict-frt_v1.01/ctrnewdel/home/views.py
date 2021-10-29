# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, CreateUserForm
#from .models import PostInput
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import views as auth_views
from biometrics.models import PostInput




#@login_required(login_url="/login/")
def index(request):
    	context = {'segment': 'index'}

    	html_template = loader.get_template('home/home.html')
    	return HttpResponse(html_template.render(context, request))

def admindash(request):
    context = {''}

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:attendance')

        else:
            return render(request, 'home/register.html', context={'messages':messages.get_messages(request)})

    return render(request = request,
                  template_name = "home/login.html",
                  context={})

@csrf_exempt
def register_user(request):
    msg = None
    success = False
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")


            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return render(request, 'home/login.html')

        else:
            msg = 'Form is not valid'
    else:
        form = CreateUserForm()

    return render(request, "home/register.html", {"form": form, "msg": msg, "success": success})

def attendance(request):
    attendance = PostInput.objects.all

    context ={'attendance': attendance}

    return render(request,"home/index.html", context)
