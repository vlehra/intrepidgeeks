from django.db import models
from django.urls import reverse 
# Create your models here.
class Mentor(models.Model):
	Name    = models.CharField(max_length = 35)
	College   = models.CharField(max_length = 35)
	header_pic =  models.ImageField(upload_to='upload_images/', blank=False)
	profile_pic = models.ImageField(upload_to='upload_images/', blank=False)
	Course1   = models.CharField(max_length = 35)
	Course2   = models.CharField(max_length = 35, blank=True,null=True)
	Course3   = models.CharField(max_length = 35, blank=True, null=True)
	Course4   = models.CharField(max_length = 35, blank=True, null=True)
	Course5   = models.CharField(max_length = 35, blank=True, null=True)
	Speciality = models.CharField(max_length = 35, blank=True, null=True)
	job   = models.CharField(max_length = 35, null=True)
	Contact_no   = models.CharField(max_length=12, unique=True)
	facebook = models.URLField()
	insta = models.URLField()
	twitter = models.URLField()
	Description = models.TextField(blank=True, null=True)
	

	def __str__(self):
		return self.Name

	def get_absolute_url(self):
		return reverse("mentordetails", kwargs={"id": self.id})