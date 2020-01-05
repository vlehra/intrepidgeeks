from django import forms
from mentorship.models import Mentor
from phonenumber_field.formfields import PhoneNumberField
from Blog.models import Blog
from videos.models import Videos
from podcast.models import Writer,Episode,AudioFile
from django.conf import settings
from django.contrib.auth.models import User
from timezone_field import TimeZoneFormField


class RawBlogForm(forms.ModelForm):
	class Meta:
		model =  Blog
		fields = ('Title', 'Header_pic','first_para','Second_para','Image_1','Third_para','Image_2','Fourth_para','Fifth_para','Image_3','Sixth_para','Counselling','opportunites','time_manag','self_dev','mfitness','acadmics','tech_skills','events','writer',)

class RawMentorForm(forms.ModelForm):
	class Meta:
		model =  Mentor
		fields = ('header_pic','Name', 'College','profile_pic','Course1','Course2','Course3','Course4','Course5','Speciality','job','Contact_no','facebook','insta','twitter','Description')



class RawVideoForm(forms.ModelForm):
	class Meta:
		model =  Videos
		fields = ('link','Name', 'Thumbnail','Description1','Description2','Description3')

class RawauthorForm(forms.ModelForm):
	class Meta:
		model = Writer
		fields = ('Name', 'profile','Description','facebook','insta','twitter')


class RawepisodeForm(forms.ModelForm):
	class Meta:
		model = Episode
		fields = ('Episodes_name','Name', 'audio_file','cover','speaker')


class RawPodcastForm(forms.ModelForm):
	class Meta:
		model = AudioFile
		fields = ('Episodes','Name', 'audio_file','cover','speaker')
		 
	#serial = forms.CharField(label='serial')
	'''link = forms.URLField()
	Name = forms.CharField(label='Name', widget=forms.TextInput(attrs={"placeholder": "Your video Name"}))
	Thumbnail = forms.ImageField()
	Description1 = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Description2 = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Paragraph 2",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Description3 = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Paragraph 2",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )'''
'''	
	"""Image upload form."""
class ImageUploadForm(forms.ModelForm):
	class Meta:
		model =  Blog
		fields = ('Title', 'Header_pic',
	Title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your Blog Title"}))
	Header_pic = forms.ImageField()
	first_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Second_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Image_1 = forms.ImageField()
	Third_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Fourth_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Image_2 = forms.ImageField()
	Image_3 = forms.ImageField()
	Fifth_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	Sixth_para = forms.CharField(
		                required=False,
		                widget=forms.Textarea(
		                	    attrs={
		                	         "placeholder":"Your description",
		                	         "rows": 10,
		                	         "cols": 60
		                	    }

		                	)
		                )
	writer = forms.ModelChoiceField(queryset= User.objects.all())
  #  Title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
'''
'''
'''
