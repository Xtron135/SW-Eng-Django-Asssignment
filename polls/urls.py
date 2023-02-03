from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id_soalan>/', views.detail, name='detail'),
	path('<int:id_soalan>/results/', views.results, name='results'),
	path('<int:id_soalan>/undi/', views.undi, name='undi'),
]
