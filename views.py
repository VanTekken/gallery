from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import FileUpload, Backgrounds
from django.template import loader

# Create your views here.
def index(request):
	#latest_images = FileUpload.objects.order_by('-date_added')[:4]
	images = FileUpload.objects.all()
	background = Backgrounds.objects.all()
	template = loader.get_template('gallery/index.html')
	#template = loader.get_template(background[0].template_url)
	params = {
		'images': images,
		'background': background.filter(selected=True).template_url,
	}
	return HttpResponse(template.render(params,request))

def desc(r):
	q = r.GET.get('desc', None)
	data = {
		'query':q
	}
	return JsonResponse(q)
