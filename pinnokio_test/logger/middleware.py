#-*- coding: utf8 -*-

from pinnokio_test.logger.models import RequestEntry


class RequestLoggerMiddleware(object):
    """ Middleware for saving requests objects in database """

    def process_request(self, request):
        path = request.path
        method = request.method
        get_data = request.GET
        post_data = request.POST
        meta_data = request.META
        host = request.get_host()
        user_agent = request.META.get('HTTP_USER_AGENT', 'N/A')
        req = RequestEntry(path=path,
                           method=method,
                           get_data=get_data,
                           post_data=post_data,
                           meta_data=meta_data,
                           host=host,
                           user_agent=user_agent)
        req.save()

        return None
