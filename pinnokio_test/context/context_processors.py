#-*- coding: utf8 -*-

from django.conf import settings


def settings_context_processor(request):
    """ Processor to add django settings into context """

    return {'settings': settings}
