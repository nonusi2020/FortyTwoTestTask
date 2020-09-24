from django.db import models
from PIL import Image
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    dateofbirth = models.DateField()
    bio = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    jabber = models.CharField(max_length=100, blank=True, null=True)
    skype = models.CharField(max_length=100, blank=True, null=True)
    othercontacts = models.CharField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('update_contact', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
        size = (200, 200)
        if self.photo and (self.photo.width != 200 or self.photo.height != 200):
            filename = self.photo.path
            image = Image.open(filename)
            image.thumbnail(size, Image.ANTIALIAS)
            image.save(filename)


class Request(models.Model):
    """
    Request datamodel
    """
    path = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
