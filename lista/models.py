#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Goal(models.Model):
	nombre = models.CharField(max_length=50, help_text='Nombre de la goal.')
	tiempo_resgitro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre

class Lista(models.Model):
	usuario = models.ForeignKey(User)
	goals = models.ManyToManyField(Goal, related_name='goal', blank=True)
	nombre = models.CharField(max_length=100, help_text='Nombre de la lista.')
	imagen_head = models.ImageField(upload_to='headers', verbose_name='Headers', blank=True)
	tiempo_registro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre

class Prueba(models.Model):
	goal = models.ForeignKey(Goal)
	texto = models.TextField(help_text='Texto con una descripción de prueba.', blank=True)
	imagen = models.ImageField(upload_to='imagenes', verbose_name='Imagen', blank=True)
	video = models.TextField(help_text='Liga de YouTube.', blank=True)
	tiempo_resgitro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.goal

admin.site.register(Lista)
admin.site.register(Goal)
admin.site.register(Prueba)

admin.autodiscover()