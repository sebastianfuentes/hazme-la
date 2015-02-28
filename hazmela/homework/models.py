from django.db import models
from usuarios import Userwdt
# Create your models here.
class Homework(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=144) #como-twittah
	publishedDate = models.DateTimeField('date published')
	document =	models.FileField(upload_to='documents/%Y/%m/%d')
	status = models.IntegerField()
	dueDate = models.DateTimeField('due date')
	wdt = models.ForeignKey(Userwdt)
	CATEGORY_CHOICES(
		(MATH,'Matematicas'),
		(HISTORY,'Historia'),
		(BIOLOGY,'Biologia'),
		(LITERATURE,'Literatura'),
		(CHEMISTRY,'Quimica'),
		(FISICS,'Fisica'),
		(OTHER,'Tareas Pendejas')
		)
	category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='Matematicas')
	LEVEL_CHOICES(
		(PRIMEROPREPA,'1° de Preparatoria'),
		(SEGUNDOPREPA,'2° de Preparatoria'),
		(TERCEROPREPA,'3° de Preparatoria'),
		(PRIMEROMEDIASUP,'1° semestre de Media Superior'),
		(SEGUNDOMEDIASUP,'2° semestre de Media Superior'),
		(TERCEROMEDIASUP,'3° semestre de Media Superior'),
		(CUARTOMEDIASUP,'4° semestre de Media Superior'),
		(QUINTOMEDIASUP,'5° semestre de Media Superior'),
		(SEXTOMEDIASUP,'6° semestre de Media Superior'),
		(PRIMEROUNI,'1° semestre de Superior'),
		(SEGUNDOUNI,'2° semestre de Superior'),
		(TERCEROUNI,'3° semestre de Superior'),
		(CUARTOUNI,'4° semestre de Superior'),
		(QUINTOUNI,'5° semestre de Superior'),
		(SEXTOUNI,'6° semestre de Superior'),
		(SEPTIMOUNI,'7° semestre  de Superior'),
		(OCTAVOUNI,'8° semestre de Superior'),
		(NOVENOUNI,'9° semestre de Superior'),
		(DECIMOUNI,'10° semestre de Superior')
		)
	category = models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='PRIMEROP')
	cost = models.IntegerField()