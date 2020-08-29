from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template.response import TemplateResponse

# Create your views here.

class Contact(TemplateView):
    template_name = "fortytwoapps/contact.html"
