from django.test import TestCase, RequestFactory
from django.urls import reverse
# Create your tests here.


class ContactViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('contact')
        self.response = self.client.get(self.url)

    def test_contact_view_render(self):
            """
            basic test for contact view to return status 200 as response
            and uses correct template
            """
            self.assertEqual(self.response.status_code, 200)
            self.assertTemplateUsed(self.response, 'fortytwoapps/contact.html')
