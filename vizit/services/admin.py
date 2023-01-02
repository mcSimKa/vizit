from django.contrib import admin

# Register your models here.
from .models import Service, ServiceLocation, Address

admin.site.register(Service)
admin.site.register(Address)
admin.site.register(ServiceLocation)