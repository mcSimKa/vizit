from django.contrib import admin
from .models import Language,Country, Address
# Register your models here.
admin.site.register(Address)
admin.site.register(Language)
admin.site.register(Country)