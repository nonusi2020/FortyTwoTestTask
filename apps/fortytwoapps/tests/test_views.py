from django.test import TestCase
from django.urls import reverse
from apps.fortytwoapps.models import Contact


class ContactViewTestCase(TestCase):

    def setUp(self):

        Contact.objects.create(name='nonu',
                               lastname='si',
                               dateofbirth='1983-01-01',
                               bio='software developer',
                               email='nonu.si2020@gmail.com',
                               jabber='nonusi@42cc.co',
                               skype='nonu.si2020@gmail.com',
                               othercontacts='none')
        self.contact = Contact.objects.first()
        self.url = reverse('contact')
        self.response = self.client.get(self.url)
        self.fields = ('name', 'lastname', 'bio', 'email', 'jabber', 'skype',
                       'othercontacts')

    def test_contact_view_render(self):
        '''
        basic test for contact view to return status 200 as response
        and uses correct template
        '''
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'fortytwoapps/contact.html')

    def test_contact_view_context(self):
        '''
        test to check contact view returns contact as context.
        '''
        for field in self.fields:
            self.assertContains(self.response, getattr(self.contact, field))
