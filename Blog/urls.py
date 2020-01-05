from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

     
    
    path('', views.blog_view, name= 'blog'),
    path('add', views.blog_add, name= 'addblog'),
    path('<int:id>', views.blog_details, name= 'blogdetails'),
    
   
]