from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    dateofbirth = models.DateField()
    bio = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    jabber = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    othercontacts = models.CharField(max_length=500, blank=True, null=True)


class Request(models.Model):
    """
    Request datamodel
    """
    path = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']


class ModelsLog(models.Model):
    """
    ObjectLog Data Model
    """
    appname = models.CharField(max_length=100)
    objectname = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
