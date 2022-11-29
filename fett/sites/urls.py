from django.contrib import admin
from django.urls import path
from sites import views

urlpatterns = [

    path('data/',views.freelancerView),
  
]