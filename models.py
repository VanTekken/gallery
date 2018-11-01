from django.db import models

# Create your models here.
class FileUpload(models.Model):

	image_text = models.CharField(max_length=200)
	image = models.FileField(upload_to='media/')
	date_added = models.DateTimeField('date published')

	def __str__(self):
		return self.image_text

class Background(models.Model):
	background_name = models.CharField(max_length=200)
	template_url = models.CharField(max_length=200)

	def __str__(self):
		return self.background_name
