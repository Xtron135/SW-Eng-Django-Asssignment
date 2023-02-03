from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Soalan, Pilihan

# Create your views here.
def index(request):
	list_soalan = Soalan.objects.order_by('-tarikh_soalan')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'list_soalan': list_soalan,
	}
	return HttpResponse(template.render(context, request))

def detail(request, id_soalan):
	soalan = get_object_or_404(Soalan, pk=id_soalan)
	return render(request, 'polls/detail.html', {'soalan': soalan})

def results(request, id_soalan):
	response = "Sekarang results soalan %s."
	return HttpResponse(response % id_soalan)

def undi(request, id_soalan):
	soalan = get_object_or_404(Soalan, pk=id_soalan)
	try:
		dipilih = soalan.choice_set.get(pk=request.POST['pilihan'])
	except (KeyError, Pilihan.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'soalan': soalan,
			'error_message': "Dak awat tak pilih, orang suruh pilih",
		})
	else:
		dipilih.undi += 1
		dipilih.save()
		return HttpResponseRedirect(reverse('polls:results', args=(soalan.id,)))
