from django.urls import reverse
from apps.fortytwoapps.models import Request


def Requestlogger(get_response):
    """
    Middleware class to log requests into db
    """

    def middleware(request):
        viewed = request.path == reverse('request')
        # create request only if it is not ajax request.
        if not request.is_ajax():
            Request.objects.create(
                url=request.path,
                viewed=viewed
            )

        return get_response(request)

    return middleware
