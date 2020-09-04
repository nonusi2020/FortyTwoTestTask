from django.test import TestCase, RequestFactory
from apps.fortytwoapps.models import Contact
from apps.fortytwoapps.views import ContactView


class ContactViewTestCase(TestCase):

    def setUp(self):
        Contact.objects.all().delete()
        Contact.objects.create(name='nonu',
                               lastname='si',
                               dateofbirth='1983-01-01',
                               bio='software developer',
                               email='nonu.si2020@gmail.com',
                               jabber='nonusi@42cc.co',
                               skype='nonu.si2020@gmail.com',
                               othercontacts='none')
        self.contact = Contact.objects.first()
        self.url = '/contact/1'
        self.response = self.client.get(self.url)
        self.fields = ('name', 'lastname', 'bio', 'email', 'jabber', 'skype',
                       'othercontacts')
        self.factory = RequestFactory()

    def test_contact_view_render(self):
        '''
        basic test for contact view to return status 200 as response
        and uses correct template
        '''
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'fortytwoapps/contact_detail.html')
        self.assertEqual(self.response.context['contact'], self.contact)

    def test_contact_view_context(self):
        '''
        test to check contact view returns contact as context.
        '''
        for field in self.fields:
            self.assertContains(self.response, getattr(self.contact, field))

    def test_contact_view_no_data_in_db(self):
        """
        Test index view when there is no data in db
        """
        Contact.objects.all().delete()
        contact = Contact.objects.first()
        self.assertEqual(Contact.objects.count(), 0)
        self.response = self.client.get(self.url)
        self.assertEqual(contact, None)

    def test_more_then_one_record_in_db(self):
        """Test contact view, should return first entry from the DB"""
        Contact.objects.create(name='test1', lastname='test',
                               dateofbirth='1983-01-01')
        resp = self.client.get(self.url)
        contacts = Contact.objects.all()
        self.assertTrue(Contact.objects.count(), 2)
        self.assertEqual(contacts[0], resp.context_data['contact'])

    def test_contact_view_correct_template_status(self):
        '''
        test for contact view for correct status code and correct
        template used
        '''
        request = self.factory.get('/contact/1/')
        response = ContactView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
