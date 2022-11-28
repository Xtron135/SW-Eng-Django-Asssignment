import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Soalan(models.Model):
	ayat_soalan = models.CharField(max_length=200)
	tarikh_soalan = models.DateTimeField('date published')
	def __str__(self):
		return self.ayat_soalan
	def soalan_baru(self):
		return self.tarikh_soalan >= timezone.now() - datetime.timedelta(days=1)


class Pilihan(models.Model):
	soalan = models.ForeignKey(Soalan, on_delete=models.CASCADE)
	ayat_pilihan = models.CharField(max_length=200)
	undian = models.IntegerField(default=0)
	def __str__(self):
		return self.ayat_pilihan
