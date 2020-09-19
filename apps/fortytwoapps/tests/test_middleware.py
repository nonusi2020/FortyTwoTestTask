from django.test import TestCase
from apps.fortytwoapps.models import Request


class TestMiddleWare(TestCase):

    def setUp(self):
        Request.objects.all().delete()

    def test_request_logged_in_db(self):
        """
        Test if request that are being made are getting logged in db
        """
        self.response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(Request.objects.all().count(), 1)

    def test_nopage_request_logged_in_db(self):
        """
        Test if request made to wrong page is getting logged
        """
        self.assertEqual(self.client.get('nopage/').status_code, 404)
        self.assertEqual(Request.objects.all().count(), 1)

    def test_correct_data_stored_in_db(self):
        """
        Test if correct values are stored for respective requests
        """
        self.client.get('/')
        self.assertEqual(Request.objects.all().count(), 1)
        self.assertEqual(Request.objects.first().url, '/')
        self.assertEqual(Request.objects.first().method, 'GET')
        self.assertEqual(Request.objects.first().viewed, False)
