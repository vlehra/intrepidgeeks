from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
	if request.method == 'POST':
		user= auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'frame/login.html', {'error':'username or password is incorrect'})
	else:
	    return render(request, 'frame/login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')
	

def home_view(request):
	
	return render(request, "frame/home.html", {})