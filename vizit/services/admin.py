from django.contrib import admin

# Register your models here.
from .models import ServiceCategory, Service, Company, Address, CompanyLocation, CompanyServices, Qualification
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(CompanyLocation)
admin.site.register(CompanyServices)
admin.site.register(Qualification)