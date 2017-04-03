from django.db import models
from django.core.urlresolvers import reverse

class Estudiante(models.Model):
	"""estudiantes"""
	nombre=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.nombres+" "+self.apellidos

class Materia(models.Model):
	"""materias"""
	nombre=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.nombre