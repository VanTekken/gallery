from django.db import models

# Create your models here.
class Images(models.Model):

	title = models.CharField(max_length=200)
	filename = models.FileField(upload_to='media/')
	date_added = models.DateTimeField('date published')

	def __str__(self):
		return self.image_text

class ThemesManager(models.Manager):
	def create_theme(self, nme, url, sld):
		theme = self.create(nme=nme,url=url,sld=sld)
		return theme

class Themes(models.Model):
	#selection = models.ForeignKey('BackgroundSelection', on_delete=models.CASCADE)
	nme = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	sld = models.BooleanField(default=False)

	objects = ThemesManager()
	def __str__(self):
		return self.nme

	#SELECTION = models.ForeignKey('Backgrounds', on_delete=models.CASCADE)
	#BACKGROUND_OPTS = ((template_url, background_name),)

theme1 = ["Particles-js","gallery/particles.html",False]
theme2 = ["Plasma-js","gallery/plasma.html",True]
def db_test(name):
	q = Themes.objects.filter(nme=name)
	if len(q)>=1:
		return True
	else:
		return False

if db_test(theme1[0]):
	pass
else:
	theme = Themes.objects.create_theme("Particles-js","gallery/particles.html",False)
	
if db_test(theme2[0]):
	pass
else:
	theme = Themes.objects.create_theme("Plasma-js","gallery/plasma.html",True)

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