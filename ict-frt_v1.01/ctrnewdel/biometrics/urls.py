from django.urls import path
from django.urls import path, re_path

from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "biometrics"

urlpatterns = [

    # The home page
    path("/mobile", views.storedata, name='storedata'),
