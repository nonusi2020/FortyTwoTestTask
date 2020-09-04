from django.views.generic import DetailView
from apps.fortytwoapps.models import Contact


class ContactView(DetailView):
    model = Contact
