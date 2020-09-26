from django.test import TestCase, RequestFactory
from apps.fortytwoapps.models import Contact, Request
from apps.fortytwoapps.views import ContactView
from django.urls import reverse
from json import loads


class ContactViewTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        self.contact = Contact.objects.create(
            id=1,
            name='nonu',
            lastname='si',
            dateofbirth='1983-01-01',
            bio='software developer',
            email='nonu.si2020@gmail.com',
            jabber='nonusi@42cc.co',
            skype='nonu.si2020@gmail.com',
            othercontacts='none'
        )

        self.url = reverse('contact_default')

    def test_contact_view_render(self):
        """
        basic test for contact view to return status 200 as response
        and uses correct template
        """
        response = self.client.get(self.url, args=[1])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fortytwoapps/contact_detail.html')
        self.assertEqual(response.context['contact'], self.contact)

    def test_contact_view_context(self):
        """
        test to check contact view returns contact as context.
        """
        response = self.client.get(self.url)
        fields = ('name', 'lastname', 'bio', 'email',
                  'jabber', 'skype', 'othercontacts')
        for field in fields:
            self.assertContains(response, getattr(self.contact, field))

    def test_contact_view_no_data_in_db(self):
        """
        Test index view when there is no data in db
        """
        Contact.objects.all().delete()
        contact = Contact.objects.first()
        self.assertEqual(Contact.objects.count(), 0)
        self.assertEqual(contact, None)

    def test_more_then_one_record_in_db(self):
        """
        Test contact view, should return first entry from the DB
        """
        Contact.objects.create(name='test1', lastname='test',
                               dateofbirth='1983-01-01')
        response = self.client.get(self.url)
        contacts = Contact.objects.all()
        self.assertTrue(Contact.objects.count(), 2)
        self.assertEqual(contacts[0], response.context_data['contact'])

    def test_contact_view_correct_template_status(self):
        """
        test for contact view for correct status code and correct
        template used
        """
        factory = RequestFactory()
        request = factory.get(self.url)
        response = ContactView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)


class RequestViewTestCase(TestCase):

    def setUp(self):
        Request.objects.all().delete()

    def test_request_view_render(self):
        """
        basic test for request view to return status 200 as response
        and uses correct template
        """
        request_url = reverse('request')
        response = self.client.get(request_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fortytwoapps/requests.html')

    def test_max_10_requests_returned(self):
        """
        Test to check if there are more than 10 request in db only 10 are returned
        """
        for _ in range(11):
            self.client.get('/')

        response = self.client.get(reverse('request'))
        self.assertEqual(len(response.context_data['object_list']), 10)

    def test_requests_returned_by_ajax(self):
        """
        Test the AJAX requests made by browser
        """
        for _ in range(11):
            self.client.get('/')
        response = self.client.get('/request/?focus=true', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        request_list = loads(response.content)['request_list']
        self.assertEqual(len(request_list), 10)
        self.assertTrue(all(r.viewed for r in Request.objects.all()))

    def test_not_viewed_requests_by_ajax(self):
        """
        Test for checking correct notviewed values returned for ajax requests
        """
        for _ in range(21):
            self.client.get('/')
        response = self.client.get('/request/?focus=false', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertFalse(all(r.viewed for r in Request.objects.all()))
        new_requests = loads(response.content)['new_requests']
        self.assertEqual(new_requests, 21)


class TestUpdateContactView(TestCase):

    def test_update_contact_view_render(self):
        """
        Test to check if view is retrning
        correct template
        """
        url = reverse('update_contact', kwargs={'pk': 1})
        self.client.login(username='admin', password='admin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fortytwoapps/update_contact.html')

    def test_update_contact_view_unauthorised(self):
        """
        Test if unauthorised request is redirected to login page
        """
        self.client.logout()
        url = reverse('update_contact', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', self.response.url)
