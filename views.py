from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import FileUpload
from django.template import loader

# Create your views here.
def index(request):
	#latest_images = FileUpload.objects.order_by('-date_added')[:4]
	latest_images = FileUpload.objects.all()
	template = loader.get_template('gallery/index.html')
	params = {	
		'latest_images': latest_images,
		'n' : range(2),
	}
	nwide = 0
	return HttpResponse(template.render(params,request))

def desc(r):
	q = r.GET.get('desc', None)
	data = {
		'query':q
	}
	return JsonResponse(q)
