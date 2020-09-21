from django.views.generic import DetailView, ListView
from apps.fortytwoapps.models import Contact, Request
from django.http import HttpResponse
from json import dumps


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
        for request in requestlist:
            request['time'] = request['time'].strftime('%b %d %Y %H:%M:%S')
        if self.request.is_ajax():
            # if user is view page and getting updated by ajax set all requests to be viewed
            if self.request.GET.get('focus') == 'true':
                Request.objects.filter(viewed=False).update(viewed=True)

            context = {'new_requests': Request.objects.filter(viewed=False).count(), 'request_list': list(requestlist)}
            return HttpResponse(dumps(context), content_type="application/json")

        return super(RequestView, self).get(request, *args, **kwargs)
