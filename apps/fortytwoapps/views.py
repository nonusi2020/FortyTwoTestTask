from django.views.generic import DetailView, ListView
from apps.fortytwoapps.models import Contact, Request


class ContactView(DetailView):
    model = Contact
    # define custom method to return contact view

    def get_object(self, **kwargs):
        return Contact.objects.get(id=self.kwargs.get('pk', 1))


class RequestView(ListView):
    model = Request
    template_name = "fortytwoapps/requests.html"
    queryset = Request.objects.values()[:10]
