#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Lista(models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=100, help_text='Nombre de la lista.')
	imagen_head = models.ImageField(upload_to='headers', verbose_name='Headers', blank=True)
	tiempo_registro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre

class Goal(models.Model):
	nombre = models.CharField(max_length=50, help_text='Nombre de la goal.')
	tiempo_resgitro = models.DateTimeField(auto_now=True)
	lista = models.ForeignKey(Lista)

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

class Usuario(models.Model):
	user_id = models.ForeignKey(User)
	bio = models.TextField(help_text='Biografia del usuario.', blank=True)
	avatar = models.ImageField(upload_to='avatar', verbose_name='Avatar', blank=True)
	website = models.CharField(max_length=100, help_text='Sitio Web.', blank=True)
	ubicacion = models.CharField(max_length=100, help_text='Ubicación del usuario.', blank=True)

	def __unicode__(self):
		return self.bio

admin.site.register(Lista)
admin.site.register(Goal)
admin.site.register(Prueba)
admin.site.register(Usuario)

admin.autodiscover()