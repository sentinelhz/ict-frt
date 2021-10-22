from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import PostInput
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def savedata(request):

    if request.method == "POST":
        post = PostInput()
        data = json.loads(request.body.decode("utf-8"))
        post.name = data["name"]
        post.date = data["date"]
        post.hour = data["hour"]
        post.save()
        return HttpResponse(200, "saved")
    return HttpResponse(400)
