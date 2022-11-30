from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	
	# ex: /app/id/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /app/id/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /app/id/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
