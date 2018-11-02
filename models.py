from django.db import models

# Create your models here.
class Images(models.Model):

	title = models.CharField(max_length=200)
	filename = models.FileField(upload_to='media/')
	date_added = models.DateTimeField('date published')

	def __str__(self):
		return self.image_text

class Themes(models.Model):
	#selection = models.ForeignKey('BackgroundSelection', on_delete=models.CASCADE)
	nme = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	sld = models.BooleanField(default=False)

	def __str__(self):
		return self.nme

	#SELECTION = models.ForeignKey('Backgrounds', on_delete=models.CASCADE)
	#BACKGROUND_OPTS = ((template_url, background_name),)



'''
class Themes(models.Model):
	name = models.CharField(max_length=200)
	directory = models.Charfield(max_length=200)

	#HOMEPAGE = 'gallery/index.html'
	#page_name = 'Particles-js'

	Need to add background options here and push them into choices for the page model
	
	PAGE_CHOICES = (
		(HOMEPAGE, page_name),
	)
	
	page = models.CharField(max_length=10, choices=PAGE_CHOICES, default=PAGE_CHOICES[0])
	
	def __str__(self):
		return self.name
'''