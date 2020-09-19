from django.views.generic import DetailView, TemplateView
from apps.fortytwoapps.models import Contact


class ContactView(DetailView):
    model = Contact
    # define custom method to return contact view

    def get_object(self, **kwargs):
        return Contact.objects.get(id=self.kwargs.get('pk', 1))


class RequestView(TemplateView):
    template_name = "fortytwoapps/requests.html"
