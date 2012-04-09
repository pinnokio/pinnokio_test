from datetime import date

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.test import TestCase

from pinnokio_test.contact.models import Person


class ContactTestCase(TestCase):
    fixtures = ['test_data.json']
    PERSON_CONTEXT = 'person'
    TEST_PERSON = {'first_name': 'Ivan', 'last_name': 'Ivanoff',
                   'date_of_birth': date(1970, 1, 10), 'bio': 'Test bio',
                   'email': 'tester@mail.com', 'jid': 'tester@jabber.com',
                   'skype_id': 'tester', 'other_contacts': 'Other contacts'}

    def setUp(self):
        super(ContactTestCase, self).setUp()
        self.response = self.client.get(reverse('index'))

    def test_model(self):
        """Testing for quantity of persons"""

        self.assertEqual(Person.objects.all().count(), 1)

    def test_person_from_db(self):
        """Testing for proper data in database"""

        test_person = get_object_or_404(Person, pk=1)
        self.assertDictContainsSubset(self.TEST_PERSON, test_person.__dict__)

    def test_html_representation(self):
        """Testing for proper representing data from db on page"""

        self.assertEqual(self.response.status_code, 200)

        for key in self.TEST_PERSON.keys():
            content = self.TEST_PERSON[key]
            if key == 'date_of_birth':
                content = content.strftime('%Y-%m-%d')
            self.assertContains(self.response, content)
