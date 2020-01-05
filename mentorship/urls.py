from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

     
    
    path('', views.service_view, name= 'mentors_home'),
    path('our_mentors', views.our_mentors, name= 'mentors'),
    path('addmentor', views.addmentor, name= 'addmentors'),
    path('<int:id>', views.mentor_details, name= 'mentordetails'),
    
    
   
]