from django.shortcuts import render
from django.http import HttpResponse
from gallery.models import Images, Themes
from django.template import loader

# Create your views here.
def index(request):
	#latest_images = FileUpload.objects.order_by('-date_added')[:4]
	x = Images.objects.all()
	y = Themes.objects.filter(sld=True)[0]
	z = loader.get_template(y.url)
	#template = loader.get_template(background[0].template_url)

	params = {
		'images': x,
		'background': y.url,
	}
	return HttpResponse(z.render(params,request))

def desc(r):
	q = r.GET.get('desc', None)
	data = {
		'query':q
	}
	return JsonResponse(q)
