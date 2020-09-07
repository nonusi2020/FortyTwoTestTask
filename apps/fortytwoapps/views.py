from django.views.generic import DetailView
from apps.fortytwoapps.models import Contact


class ContactView(DetailView):
    model = Contact
    # define custom method to return contact view

    def get_object(self, **kwargs):
        if not self.kwargs:
            obj = Contact.objects.get(id=1)
        else:
            obj = Contact.objects.get(id=self.kwargs['pk'])

        return obj
