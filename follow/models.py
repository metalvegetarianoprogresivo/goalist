#encoding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, unique=True, related_name='user')
	follows = models.ManyToManyField('self', related_name='follow', symmetrical=False, blank=True)
	bio = models.TextField(help_text='Biografia del usuario.', blank=True)
	avatar = models.ImageField(upload_to='avatar', verbose_name='Avatar', blank=True)
	website = models.CharField(max_length=100, help_text='Sitio Web.', blank=True)
	ubicacion = models.CharField(max_length=100, help_text='Ubicación del usuario.', blank=True)

	def __unicode__(self):
		return unicode(self.user)

admin.site.register(Profile)

admin.autodiscover()