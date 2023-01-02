from django.db import models

# Create your models here.
class Service(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=32)
    Address = models.CharField(max_length=100)
    url = models.URLField()

class Address(models.Model):
    CityName = models.CharField(max_length=100)
    StreetName = models.CharField(max_length=100)
    Building = models.CharField(max_length=12)
    Room = models.CharField(max_length=5)

class ServiceLocation(models.Model):
    ServiceId = models.ForeignKey(Service, on_delete=models.CASCADE)
    AddressId = models.ForeignKey(Address, on_delete=models.CASCADE)
