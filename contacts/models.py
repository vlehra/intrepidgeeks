from django.db import models

# Create your models here.
class Contact_us(models.Model):
	Name    = models.CharField(max_length = 35)
	Email   = models.CharField(max_length = 35)
	Contact_no   = models.CharField(max_length=12)
	Message = models.TextField(blank=True, null=True)	

	def __str__(self):
		return self.Name