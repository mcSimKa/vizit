from django.db import models
from geodata.models import Address, Country, Language

#general dictionaries 
''' ServiceCategories category to group services on general level like {'car service','dentist','beauty cetre'} '''
class ServiceCategory(models.Model):
    name = models.CharField(max_length=64)
   
    def __str__(self):
        return self.name

#master qualification =
''' Qaulifications is master specific category {'dentist','surgery','master of manicure','barber','stylist','makeup'}'''
class Qualification(models.Model):
    title = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return self.title


'''Servcies is general category that defines global areas on the market 
   service={'manicure', 'tooth repair', 'oil replacement'}'''
class Service(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    #methods
    def __str__(self) -> str:
        return self.name +"|"+self.category.name

class Master(models.Model):
    name = models.CharField(max_length=64)
    qualification = models.ForeignKey(Qualification, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

         
class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=32)
    url = models.URLField()
    serviceCategory = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name+'('+self.url+')'


class CompanyService(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company.name+"|"+self.company.serviceCategory.categoryName+"\\"+self.service.serviceName


class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company.name+"|"+self.address.__str__()
