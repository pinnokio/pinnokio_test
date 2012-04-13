#-*- coding: utf8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('pinnokio_test.extra.views',
    url(r'^$', 'logger', name='requests_view_10'),
)
