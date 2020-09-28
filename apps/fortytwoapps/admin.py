from django.contrib import admin
from .models import Contact, Request, ModelsLog
# Register your models here.
admin.site.register(Contact)
admin.site.register(Request)
admin.site.register(ModelsLog)
