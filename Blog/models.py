from django.db import models
from django.conf import settings
from datetime import datetime 
from django.urls import reverse 

# Create your models here.
class Blog(models.Model):
	Title    = models.CharField(max_length = 35)
	Header_pic = models.ImageField(upload_to='upload_images/', blank=False, null=True)
	first_para = models.TextField(blank=False, null=True)
	Second_para = models.TextField(blank=False, null=True)
	Image_1 = models.ImageField(upload_to='upload_images/', blank=False, null=True)
	Third_para = models.TextField(blank=False, null=True)
	Image_2 = models.ImageField(upload_to='upload_images/', blank=True, null=True)
	Fourth_para = models.TextField(blank=True, null=True)
	Fifth_para = models.TextField(blank=True, null=True)
	Image_3 = models.ImageField(upload_to='upload_images/', blank=True, null=True)
	Sixth_para = models.TextField(blank=True, null=True)
	Counselling = models.BooleanField()
	opportunites = models.BooleanField()
	time_manag = models.BooleanField()
	self_dev = models.BooleanField()
	mfitness = models.BooleanField()
	acadmics = models.BooleanField()
	tech_skills = models.BooleanField()
	events = models.BooleanField()
	writer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
	pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank = True,)
	
	
	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse("blogdetails", kwargs={"id": self.id})
	
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')

	def intro(self):
		return self.first_para[:150]

	def title_intro(self):
		return self.Title[:50]
		
