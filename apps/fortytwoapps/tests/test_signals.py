from django.test import TestCase
from apps.fortytwoapps.models import Contact, ModelsLog


class TestSignals(TestCase):

    def setUp(self):
        Contact.objects.create(
            name='test',
            lastname='user',
            dateofbirth='1983-01-01',
            bio='none',
            email='nonu.si2020@test.com',
            jabber='test@42cc.co',
            skype='test.test',
            othercontacts='no'
        )

    def test_create_post_save_signal(self):
        """
        Test post Save signal for create is creating log in db
        """
        modelslog = ModelsLog.objects.last()
        self.assertEqual(modelslog.appname, 'fortytwoapps')
        self.assertEqual(modelslog.objectname, 'Contact')
        self.assertEqual(modelslog.action, 'created')

    def test_update_post_save_signal(self):
        """
        Test post Save signal for update is creating log in db
        """
        contact = Contact.objects.last()
        contact.name = 'newuser'
        contact.save()
        modelslog = ModelsLog.objects.last()
        self.assertEqual(modelslog.appname, 'fortytwoapps')
        self.assertEqual(modelslog.objectname, 'Contact')
        self.assertEqual(modelslog.action, 'updated')

    def test_delete_post_save_signal(self):
        """
        Test post Save signal for delete is creating log in db
        """
        Contact.objects.last().delete()
        modelslog = ModelsLog.objects.last()
        print(modelslog.appname, modelslog.objectname, modelslog.action)
        self.assertEqual(modelslog.appname, 'fortytwoapps')
        self.assertEqual(modelslog.objectname, 'Contact')
        self.assertEqual(modelslog.action, 'deleted')
