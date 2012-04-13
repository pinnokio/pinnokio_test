from django.shortcuts import render_to_response

from pinnokio_test.extra.models import RequestEntry


def logger(request):
    requests = RequestEntry.objects.all().order_by('creation_time')[:10]
    return render_to_response('extra/logger.html',
            {'requests': requests})
