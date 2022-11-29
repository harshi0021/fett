from django.contrib import admin
from django.urls import path
from pro import views
  
urlpatterns = [
   
    path('create/', views.add_items, name='add-items'),
    path('get/<int:pk>/', views.view_items, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('delete/<int:pk>/', views.delete_items, name='delete-items'),


]