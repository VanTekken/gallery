from django.db import models

# Create your models here.
class FileUpload(models.Model):

	image_text = models.CharField(max_length=200)
	image = models.FileField(upload_to='media/')
	date_added = models.DateTimeField('date published')

	def __str__(self):
		return self.image_text

class BackgroundSelection(models.Model):
	#HOMEPAGE = 'index.html'
	#page_name = 'Home'

	SELECTION = models.ForeignKey('Backgrounds', on_delete=models.CASCADE)

	page = models.CharField(max_length=10, choices=SELECTION, default=SELECTION)

	def __str__(self):
		return self.page_name


class Backgrounds(models.Model):
	#selection = models.ForeignKey('BackgroundSelection', on_delete=models.CASCADE)
	background_name = models.CharField(max_length=200)
	template_url = models.CharField(max_length=200)
	selected = models.BooleanField(default=False)

	def __str__(self):
		return self.background_name

	BACKGROUND_OPTS = ((template_url, background_name),)


