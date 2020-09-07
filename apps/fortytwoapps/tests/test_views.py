from django.test import TestCase, RequestFactory
from apps.fortytwoapps.models import Contact
from apps.fortytwoapps.views import ContactView
from django.urls import reverse


class ContactViewTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        self.contact = Contact.objects.create(id=1,
                                              name='nonu',
                                              lastname='si',
                                              dateofbirth='1983-01-01',
                                              bio='software developer',
                                              email='nonu.si2020@gmail.com',
                                              jabber='nonusi@42cc.co',
                                              skype='nonu.si2020@gmail.com',
                                              othercontacts='none')

        self.url = reverse('contact_default')

    def test_contact_view_render(self):
        '''
        basic test for contact view to return status 200 as response
        and uses correct template
        '''
        response = self.client.get(self.url, args=[1])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fortytwoapps/contact_detail.html')
        self.assertEqual(response.context['contact'], self.contact)

    def test_contact_view_context(self):
        '''
        test to check contact view returns contact as context.
        '''
        response = self.client.get(self.url)
        fields = ('name', 'lastname', 'bio', 'email', 'jabber', 'skype', 'othercontacts')
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
        """Test contact view, should return first entry from the DB"""
        Contact.objects.create(name='test1', lastname='test',
                               dateofbirth='1983-01-01')
        response = self.client.get(self.url)
        contacts = Contact.objects.all()
        self.assertTrue(Contact.objects.count(), 2)
        self.assertEqual(contacts[0], response.context_data['contact'])

    def test_contact_view_correct_template_status(self):
        '''
        test for contact view for correct status code and correct
        template used
        '''
        factory = RequestFactory()
        request = factory.get(self.url)
        response = ContactView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
        response = ContactView.as_view()
