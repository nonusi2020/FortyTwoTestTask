from django.views.generic import DetailView, ListView, UpdateView
from apps.fortytwoapps.models import Contact, Request
from apps.fortytwoapps.forms import UpdateContactForm
from django.http import JsonResponse


class ContactView(DetailView):
    model = Contact
    # define custom method to return contact view

    def get_object(self, **kwargs):
        return Contact.objects.get(id=self.kwargs.get('pk', 1))


class RequestView(ListView):
    model = Request
    template_name = "fortytwoapps/requests.html"
    queryset = Request.objects.values()[:10]

    def get(self, request, *args, **kwargs):
        requestlist = Request.objects.values()[:10]
        if self.request.is_ajax():
            # if user is view page and getting updated by ajax set all requests to be viewed
            if self.request.GET.get('focus') == 'true':
                Request.objects.filter(viewed=False).update(viewed=True)

            context = {'new_requests': Request.objects.filter(viewed=False).count(), 'request_list': list(requestlist)}
            return JsonResponse(context)

        return super(RequestView, self).get(request, *args, **kwargs)


class UpdateContact(UpdateView):
    model = Contact
    template_name = "fortytwoapps/update_contact.html"
    form_class = UpdateContactForm

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {'name': self.object.name}
            return JsonResponse(data)
        else:
            return response
