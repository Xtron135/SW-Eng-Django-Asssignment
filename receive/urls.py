from django.urls import path

from . import views


urlpatterns = [
	path('', views.masuk_input, name='masuk_input'),
]
