from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

     
    
    path('author/<int:id>', views.PodcastDetails, name= 'podcastdetails'),
    path('author/', views.Authors, name= 'Authors'),
    path('add_author/', views.add_authors, name= 'addauthors'),
    path('addepisode/', views.addepisode, name= 'addepisode'),
    path('', views.Podcast, name= 'podcast'),
    path('addPodCast/', views.AddPodcast, name= 'addpodcast'),
    path('episodes/<int:id>', views.EpisodeDetails, name= 'episodedetails'),
    path('episodes/', views.Episodes, name= 'episodes'),
    
   
]