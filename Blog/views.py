
from django.shortcuts import render,redirect, get_object_or_404
from inrepidgeeks.forms import RawBlogForm
from .models import Blog
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def blog_view(request):
	blog = Blog.objects.all()
	return render(request, "blogs/blog.html", {"blog":blog})

@login_required

def blog_add(request):
	form = RawBlogForm()
	if request.method == 'POST':
		form = RawBlogForm(request.POST,request.FILES)
		
		
		if form.is_valid():
			
			print(form.cleaned_data)
			Blog.objects.create(**form.cleaned_data)
			return redirect('addblog')
		else:
			print(form.errors)

	context = {
		'form': form
	}
	return render(request, "blogs/addblog.html", context)
'''
def add_particulars(request):
	form = RawParticularForm()
	if request.method == 'POST':
	    form = RawParticularForm(request.POST)
	    if form.is_valid():

		     print(form.cleaned_data)
		     Menu.objects.create(**form.cleaned_data)
		     return redirect('particulars')
	    else:
		     print(form.errors)

	context = {
	    'form': form
	}
	return render(request, "menu/add_particulars.html", context)




if request.POST['Title'] and request.FILES['Header_pic']:
			m = Blog()
			m.Title = request.POST['Title']
			m.Header_pic = request.FILES['Header_pic']
			m.first_para   = request.POST['first_para']
			m.Second_para = request.POST['Second_para']
			m.Image_1 = request.FILES['Image_1']
			m.Third_para = request.POST['Third_para']
			m.Fourth_para = request.POST['Fourth_para']
			m.Image_2 = request.FILES['Image_2']
			m.Image_3 = request.FILES['Image_3']
			m.Fifth_para = request.POST['Fifth_para']
			m.Sixth_para = request.POST['Sixth_para']
			m.Counselling = request.POST['Counselling']
			m.opportunites = request.POST['Opportunities']
			m.time_manag = request.POST['Time_m']
			m.self_dev = request.POST['Self_dev']
			m.mfitness = request.POST['Mental_fit']
			m.acadmics = request.POST['Academics']
			m.tech_skills = request.POST['Technical']
			m.events = request.POST['Events']
			m.writer = request.user
			m.pub_date = timezone.datetime.now()

			m.save()
			return redirect('blog')
'''


'''
	def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')'''




def blog_details(request, id):
	obj = get_object_or_404(Blog, id= id)
	blog = Blog.objects.all()
	context = {
	    "object": obj,
	    "blog":blog,
	}
	return render(request, 'blogs/blogs_details.html', context)

