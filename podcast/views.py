from django.shortcuts import render,redirect, get_object_or_404
from .models import AudioFile,Writer,Episode
from django.db.models import Q
from django.urls import reverse 
from inrepidgeeks.forms import RawauthorForm,RawepisodeForm,RawPodcastForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def PodcastDetails(request, id):
	obj = AudioFile.objects.all()
	ob = get_object_or_404(Writer, id= id)
	#node = AudioFile.objects.filter(Q(Writer) | Q(collaborators=Writer)).select_related('speaker').distinct()
	ep = Episode.objects.all()
	
	context = {
	    "object": obj,
	    "ob": ob,
	    "ep": ep,
	    #"node": node,
	   
	}
	return render(request, 'podcast/podcastlist.html', context)


def Podcast(request):
	obj = AudioFile.objects.all()
	ob = Writer.objects.all()
	ep = Episode.objects.all()
	context = {
	    "object": obj,
	    "ob": ob,
	    "ep": ep,
	}
	return render(request, 'podcast/podcast.html', context)


def Authors(request):
	obj = AudioFile.objects.all()
	ob = Writer.objects.all()
	ep = Episode.objects.all()
	context = {
	    "obj": obj,
	    "ob": ob,
	    "ep": ep,
	}
	return render(request, 'podcast/podcastauthorslist.html', context)


def EpisodeDetails(request, id):
	obj = AudioFile.objects.all()
	ep = get_object_or_404(Episode, id= id)
	ob = Writer.objects.all()
	
	context = {
	    "object": obj,
	    "ob": ob,
	    "ep": ep,
	}
	return render(request, 'podcast/episodelist.html', context)

def Episodes(request):
	ep = Episode.objects.all()
	ob = Writer.objects.all()
	obj = AudioFile.objects.all()
	context = {
	    "object": obj,
	    "ob": ob,
	    "ep": ep,
	}
	return render(request,'podcast/podcastepisodes.html',context)

@login_required
def add_authors(request):
	form = RawauthorForm()
	if request.method == 'POST':
		form = RawauthorForm(request.POST,request.FILES)
		
		
		if form.is_valid():
			
			print(form.cleaned_data)
			Writer.objects.create(**form.cleaned_data)
			return redirect('Authors')
		else:
			print(form.errors)

	context = {
		'form': form
	}
	return render(request, 'podcast/add_authors.html',context)

@login_required
def addepisode(request):
	form = RawepisodeForm()
	if request.method == 'POST':
		form = RawepisodeForm(request.POST,request.FILES)
		
		
		if form.is_valid():
			
			print(form.cleaned_data)
			Episode.objects.create(**form.cleaned_data)
			return redirect('episodes')
		else:
			print(form.errors)

	context = {
		'form': form
	}
	return render(request,'podcast/addepisode.html', context)

@login_required
def AddPodcast(request):
	form = RawPodcastForm()
	if request.method == 'POST':
		form = RawPodcastForm(request.POST,request.FILES)
		
		
		if form.is_valid():
			
			print(form.cleaned_data)
			AudioFile.objects.create(**form.cleaned_data)
			return redirect('podcast')
		else:
			print(form.errors)

	context = {
		'form': form
	}
	return render(request,'podcast/AddPodcast.html',context)