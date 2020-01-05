from django.db import models
from datetime import datetime 
from django.urls import reverse 
from django.conf import settings
# Create your models here.
class Videos(models.Model):
	Name = models.TextField(blank=True, null=True)
	Thumbnail = models.ImageField(upload_to='upload_images/', blank=False, null=True)
	link = models.URLField()
	Description1 = models.TextField(blank=True, null=True)
	Description2 = models.TextField(blank=True, null=True)
	Description3 = models.TextField(blank=True, null=True)
	writer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
	pub_date = models.DateTimeField()
	
	def summary(self):
		return self.Description[:100]
		
	def __str__(self):
		return self.Name

	def get_absolute_url1(self):
		return reverse("videodetails", kwargs={"id": self.id})


	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e, %Y')

	def title_intro(self):
		return self.Name[:50]
