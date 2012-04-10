#-*- coding: utf8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('pinnokio_test.logger.views',
    url(r'^$', 'index', name='requests_view_10'),
)
