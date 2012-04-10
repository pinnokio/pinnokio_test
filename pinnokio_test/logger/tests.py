from django.test import TestCase
from django.core.urlresolvers import reverse

from pinnokio_test.logger.models import RequestEntry


class RequestDbLoggerTest(TestCase):
    """ Test for middleware"""

    def test_save_request(self):
        """ Test for proper saving requests in database """

        entry = RequestEntry.objects.filter(path='/test_urn/')
        self.assertEqual(entry.count(), 0)
        self.client.get('/test_urn/')
        self.assertEqual(entry.count(), 1)


class RequestListViewTest(TestCase):
    """ Test for displaying requests data """

    fixtures = ['logger_test_data.json']

    def setUp(self):
        self.response = self.client.get(reverse('requests_view_10'))

    def test_requests_num(self):
        """ Testing for number of requests in database """

        requests_num = len(self.response.context['requests'])
        self.assertLessEqual(requests_num, 10)

    def  test_html_representation(self):
        """ Testing for proper displaying requests data in html page """

        self.assertEqual(self.response.status_code, 200)
        requests = RequestEntry.objects.all().order_by('creation_time')[:10]
        for request in requests:
            for key in ('creation_time', 'method', 'path'):
                self.assertContains(self.response, request.__dict__[key])
