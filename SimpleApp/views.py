from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader


from .models import Soalan

def index(request):
	return HttpResponse("The Amazing Spiders")


# List kan latest 5 object
def index(request):
	latest_list_soalan = Soalan.objects.order_by('-tarikh_soalan')[:5]
	template = loader.get_template('SimpleApp/index.html')
	context = {
	'latest_list_soalan': latest_list_soalan,
	}
	return HttpResponse(template.render(context, request))


# Setiap page utk setiap elemen: detail, result, undi, based on object id
def detail(request, question_id):
	return HttpResponse("Sekarang soalan %s." % question_id)

def results(request, question_id):
	response = "Sekarang result untuk soalan %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Sekarang undi untuk soalan %s." % question_id)
