from django.db import models
from datetime import datetime 
from django.urls import reverse 
from django.conf import settings
# Create your models here.
class Writer(models.Model):
	Name = models.CharField(max_length= 50)
	profile = models.ImageField(upload_to= 'Profile_images/')
	Description = models.TextField(blank=True, null=True)
	facebook = models.URLField()
	insta = models.URLField()
	twitter = models.URLField()
	def __str__(self):
		return self.Name
	def get_absolute_url1(self):
		return reverse("podcastdetails", kwargs={"id": self.id})



class Episode(models.Model):
    Episodes_name = models.CharField(max_length = 250)
    Name = models.CharField(max_length = 150)
    audio_file = models.FileField(upload_to="music")
    cover = models.ImageField(upload_to='upload_images/')
    speaker = models.ForeignKey(Writer,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank = True,)


    def __str__(self):
        return self.Episodes_name

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def get_absolute_url1(self):
        return reverse("episodedetails", kwargs={"id": self.id})


class AudioFile(models.Model):
    Episodes = models.ForeignKey(Episode,on_delete=models.CASCADE,)
    Name = models.CharField(max_length = 150)
    audio_file = models.FileField(upload_to="music")
    cover = models.ImageField(upload_to='upload_images/')
    speaker = models.ForeignKey(Writer,on_delete=models.CASCADE,)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank = True,)


    def __str__(self):
        return self.Name

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')



'''def get_absolute_url(self):
		return reverse("blogdetails", kwargs={"id": self.id})
	'''