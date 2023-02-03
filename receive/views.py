from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def masuk_input(request):
	if request.method == 'GET':
		mesej = request.GET.get('mesej', '')
		return HttpResponse('Mesej anda ialah: ' + mesej)
