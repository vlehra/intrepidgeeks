from django.shortcuts import render,redirect, get_object_or_404
from inrepidgeeks.forms import RawMentorForm
from .models import  Mentor
from django.contrib.auth.decorators import login_required
# Create your views here.

def service_view(request):
	return render(request, "mentorship/home.html", {})




def our_mentors(request):
	m = Mentor.objects.all()
	return render(request, "mentorship/our_mentors.html", {"m": m})

@login_required
def addmentor(request):
	form = RawMentorForm()
	if request.method == 'POST':
		form = RawMentorForm(request.POST,request.FILES)
		
		
		if form.is_valid():
			
			print(form.cleaned_data)
			Mentor.objects.create(**form.cleaned_data)
			return redirect('mentors')
		else:
			print(form.errors)

	context = {
		'form': form
	}
	return render(request,"mentorship/addmentor.html",context)

def mentor_details(request,id):
	obj = get_object_or_404(Mentor, id= id)
	m = Mentor.objects.all()
	context = {
	    "obj": obj,
	    "m":m,
	}
	return render(request,"mentorship/mentor_details.html",context )