#-*- coding: utf8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('pinnokio_test.contact.views',
    url(r'^$', 'index', name='index'),
)
