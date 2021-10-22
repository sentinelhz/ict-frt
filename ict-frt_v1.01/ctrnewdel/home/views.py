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
from .forms import LoginForm, SignUpForm
#from .models import PostInput
from django.views.decorators.csrf import csrf_exempt
import json


#@login_required(login_url="/login/")
def index(request):
    	context = {'segment': 'index'}

    	html_template = loader.get_template('home/home.html')
    	return HttpResponse(html_template.render(context, request))


@csrf_exempt
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "home/login.html", {"form": form, "msg": msg})


@csrf_exempt
def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "home/register.html", {"form": form, "msg": msg, "success": success})


    def attendance(request):

        attendance = PostInput.objects.all

        context ={'attendance': attendance}

        return render(request,"home/employeeattendance.html", context)
