from django.views.generic import TemplateView
from apps.fortytwoapps.models import Contact


class ContactView(TemplateView):
    template_name = "fortytwoapps/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        return context
