from django.test import TestCase
from apps.fortytwoapps.models import Contact
from apps.fortytwoapps.forms import UpdateContactForm


class TestUpdateContactForm(TestCase):

    def setUp(self):
        self.updatedata = {
            'name': 'test', 'lastname': 'user', 'dateofbirth': '1983-05-01', 'email': 'testuser@test.com',
            'skype': 'test.user', 'jabber': 'test@42cc.co', 'othercontacts': 'none', 'bio': 'no bio'
        }
        self.contact = Contact.objects.first()

    def test_valid_data_update_request(self):
        """
        Test for checking form with valid data
        """
        form = UpdateContactForm(self.updatedata, instance=self.contact)
        self.assertTrue(form.is_valid())
        form.save()
        fields = ('name', 'lastname', 'bio', 'email', 'jabber', 'skype', 'othercontacts')

        for field in fields:
            self.assertEqual(getattr(self.contact, field), form.data[field])

        self.assertEqual(getattr(self.contact, "dateofbirth").strftime('%Y-%m-%d'), form.data["dateofbirth"])

    def test_blank_data_update_request(self):
        """Test form validation for blank data
        """
        form = UpdateContactForm(data={}, instance=self.contact)
        self.assertFalse(form.is_valid())
        self.assertDictEqual(form.errors, {
            'dateofbirth': ['This field is required.'], 'lastname': ['This field is required.'],
            'name': ['This field is required.']
        })
