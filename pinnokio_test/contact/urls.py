#-*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('pinnokio_test.contact.views',
    url(r'^$', 'index', name='index'),
    url(r'^contact/edit/$', 'contact_edit', name='contact_edit'),
    url(r'^login/$', login, {'template_name': 'contact/login.html'},
                            name='login'),
    url(r'^logout/$', logout, name='logout'),
)
