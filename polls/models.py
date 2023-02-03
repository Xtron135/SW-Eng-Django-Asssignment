import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Soalan(models.Model):
	teks_soalan = models.CharField(max_length=200)
	tarikh_soalan = models.DateTimeField('data published')

	def __str__(self):
		return self.teks_soalan

	def baru_ke(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Pilihan(models.Model):
	Soalan = models.ForeignKey(Soalan, on_delete=models.CASCADE)
	teks_pilihan = models.CharField(max_length=200)
	undi = models.IntegerField(default=0)

	def __str__(self):
		return self.teks_pilihan
