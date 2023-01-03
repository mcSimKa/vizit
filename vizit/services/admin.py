from django.contrib import admin

# Register your models here.
from .models import ServiceCategory, Service, Company, Addresses, CompanyLocation, CompanyServices
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(Company)
admin.site.register(Addresses)
admin.site.register(CompanyLocation)
admin.site.register(CompanyServices)