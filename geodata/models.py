from django.db import models

# Create your models here.
''' Language is general category. Potentially can be linked to the service, customer, country'''
class Language(models.Model):
    name = models.CharField(max_length=64)
    tag = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name

'''Country is general category, every address should be linked to the country. 
THis enable multycountry usage of the backed'''
class Country(models.Model):
    name = models.CharField(max_length=64)
    tag = models.CharField(max_length=2)
    main_language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.name

''' Address helps to locate service on the map. Ideally it should have country'''
class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=12)
    room = models.CharField(max_length=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '('+self.city+')|('+self.street+')|('+self.building+')'