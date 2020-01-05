from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Videos
from inrepidgeeks.forms import RawVideoForm
from django.utils import timezone

# Create your views here.
def videos_view(request):
	full_list = Videos.objects.all()
	form = RawVideoForm()
	if request.method == 'POST':
		form = RawVideoForm(request.POST)
		if form.is_valid():
			
			print(form.cleaned_data)
			Videos.objects.create(**form.cleaned_data)
			return redirect('videos')
		else:
			print(form.errors)

	context = {
	    'form': form,
	    'full_list':full_list,
	}
	return render(request, "videos/videos.html", context)

@login_required

def addvideo(request):
	if request.method == 'POST':
		if request.POST['Name'] and  request.POST['link']:
			m = Videos()
			m.Name = request.POST['Name']
			m.Thumbnail = request.FILES['pic']
			m.link   = request.POST['link']
			m.Description1 = request.POST['Description1']
			m.Description2 = request.POST['Description2']
			m.Description3 = request.POST['Description3']
			m.writer = request.user
			m.pub_date = timezone.datetime.now()
			m.save()	
	return render(request, "videos/addvideo.html", {})






def video_details(request, id):
	obj = get_object_or_404(Videos, id= id)
	blog = Videos.objects.all()
	context = {
	    "object": obj,
	    "blog":blog,
	}
	return render(request, 'videos/video_details.html', context)





	