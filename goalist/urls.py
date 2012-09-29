from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from lista.views import lista, inicio, usuario, goal, search, register, registerProfile

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goalist.views.home', name='home'),
    # url(r'^goalist/', include('goalist.foo.urls')),
    url(r'^$', inicio, name='inicio'),
    url(r'^lista/([0-9]+)/$', lista, name='lista'),
    url(r'^goal/([0-9]+)/$', goal, name='goal'),
    url(r'^search/$', search, name='search'),
    url(r'^register/$', register, name='register'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^register/([a-zA-Z0-9_.-]+)/$', registerProfile, name='registerProfile'),
    url(r'^([a-zA-Z0-9_.-]+)/$', usuario, name='usuario'),
)