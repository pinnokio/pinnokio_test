from django.test import TestCase
from django.conf import settings


class SettingsContextTest(TestCase):
    """ Test for settings context processor """

    def test_context(self):
        """ Test for checking context variable"""

        response = self.client.get('requests_view_10')
        self.assertTrue('settings' in response.context)
        self.assertEqual(response.context['settings'], settings)
