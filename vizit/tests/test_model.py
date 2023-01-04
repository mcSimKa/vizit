import unittest
from django.test import TestCase
from services.models import ServiceCategory, Service, Qualification, Master


class ModelTest(TestCase):

    def test_ServiceCategoryModel(self):
        category = ServiceCategory.objects.create(name='CTO')
        self.assertEquals(str(category),'CTO')
        print("IsInstance : ", isinstance(category,ServiceCategory))
        self.assertTrue(isinstance(category,ServiceCategory))

    def test_ServiceModel(self):
        _category = ServiceCategory.objects.create(name='Beauty')
        service = Service.objects.create(name='Daniel', category=_category)
        self.assertEquals(str(service),"Daniel|Beauty")
        print("IsInstance : ", isinstance(service,Service))
        self.assertTrue(isinstance(service,Service))

    def test_QualificationModel(self):
        qualification = Qualification.objects.create(title='dentist')
        self.assertEquals(str(qualification),'dentist')
        print("IsInstance : ", isinstance(qualification,Qualification))
        self.assertTrue(isinstance(qualification,Qualification))

    def test_Master(self):
        _qualification = Qualification.objects.create(title='dentist')
        master = Master.objects.create(name="Софія Трифонівна", qualification=_qualification)
        self.assertEquals(str(master),"Софія Трифонівна")
        print("IsInstance : ", isinstance(master, Master))
        self.assertTrue(isinstance(master, Master))