"""inrepidgeeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from frame.views import home_view,login,logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('Blog.urls')),
    path('', home_view, name= 'home'),
    path('mentor-mentee/', include('mentorship.urls')),
    path('videos/', include('videos.urls')),
    path('contacts/', include('contacts.urls')),
    path('podcast/', include('podcast.urls')),
    path('login/', login, name= 'login'),
    path('logout/', logout, name= 'logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
