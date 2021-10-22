# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from home import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "home"

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),



]
