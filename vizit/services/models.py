from django.db import models

class ServiceCategory(models.Model):
    categoryName = models.CharField(max_length=64)
    
    def __str__(self):
        return self.categoryName


class Service(models.Model):
    serviceName = models.CharField(max_length=64)
    serviceCategory = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    #methods
    def __str__(self) -> str:
        return self.serviceName 

        
class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=32)
    url = models.URLField()
    serviceCategory = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name+'('+self.url+')'


class Addresses(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    building = models.CharField(max_length=12)
    room = models.CharField(max_length=5)

    def __str__(self) -> str:
        return '('+self.city+')|('+self.street+')|('+self.building+')'


class CompanyServices(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company.name+"|"+self.company.serviceCategory.categoryName+"\\"+self.service.serviceName


class CompanyLocation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE)
