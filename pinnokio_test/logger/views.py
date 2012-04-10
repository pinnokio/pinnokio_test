from django.shortcuts import render_to_response

from pinnokio_test.logger.models import RequestEntry


def index(request):
    requests = RequestEntry.objects.all().order_by('creation_time')[:10]
    return render_to_response('logger/index.html',
            {'requests': requests})
