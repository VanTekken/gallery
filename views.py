from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Images, Themes
from django.template import loader

# Create your views here.
def index(request):
	#latest_images = FileUpload.objects.order_by('-date_added')[:4]
	images = Images.objects.all()
	#background = Backgrounds.objects.all()
	theme = Themes.objects.filter(sld=True)[0].url
	#template = loader.get_template('gallery/index.html')
	template = loader.get_template(theme)
	params = {
		'images': images,
		'background': theme,
	}
	return HttpResponse(template.render(params,request))

def desc(r):
	q = r.GET.get('desc', None)
	data = {
		'query':q
	}
	#return JsonResponse(q)
