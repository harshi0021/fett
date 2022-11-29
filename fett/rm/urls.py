from django.contrib import admin
from django.urls import path
from rm import views
urlpatterns = [
   
    path('for/',views.forumview),
    path('getbyall/',views.getview),
    path('getutbyidfor/<int:pk>/',views.getputview),
]
