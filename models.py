from django.db import models

# Create your models here.
class FileUpload(models.Model):

	image_text = models.CharField(max_length=200)
	image = models.FileField(upload_to='media/')
	date_added = models.DateTimeField('date published')

	def __str__(self):
		return self.image_text

class BackgroundSelection(models.Model):
	HOMEPAGE = 'gallery/index.html'
	page_name = 'Particles-js'

	#Need to add background options here and push them into choices for the page model

	PAGE_CHOICES = (
		(HOMEPAGE, page_name),
	)

	page = models.CharField(max_length=10, choices=PAGE_CHOICES, default=PAGE_CHOICES[0])
	


	def __str__(self):
		return self.page_name


class Backgrounds(BackgroundSelection):
	#selection = models.ForeignKey('BackgroundSelection', on_delete=models.CASCADE)
	background_name = models.CharField(max_length=200)
	template_url = models.CharField(max_length=200)
	selected = models.BooleanField(default=False)

	def __str__(self):
		return self.background_name

	#SELECTION = models.ForeignKey('Backgrounds', on_delete=models.CASCADE)

	#BACKGROUND_OPTS = ((template_url, background_name),)


