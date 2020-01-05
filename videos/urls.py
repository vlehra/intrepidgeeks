from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

     
    
    path('', views.videos_view, name= 'videos'),
    path('addVideo', views.addvideo, name= 'addvideo'),
    path('<int:id>', views.video_details, name= 'videodetails'),
   # path('audio/<int:id>', views.Podcast, name= 'Podcastdetails'),
    
   
]