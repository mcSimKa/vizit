from django.contrib import admin

# Register your models here.
from .models import ServiceCategory, Service, Company, CompanyLocation, CompanyService, Qualification
    
admin.site.register(Service)
admin.site.register(ServiceCategory)
admin.site.register(Company)
admin.site.register(CompanyLocation)
admin.site.register(CompanyService)
admin.site.register(Qualification)
