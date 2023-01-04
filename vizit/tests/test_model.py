import unittest
from django.test import TestCase
from services.models import ServiceCategory, Service


class ModelTest(TestCase):

    def test_ServiceCategoryModel(self):
        category = ServiceCategory.objects.create(categoryName='CTO')
        self.assertEquals(str(category),'CTO')
        print("IsInstance : ", isinstance(category,ServiceCategory))
        self.assertTrue(isinstance(category,ServiceCategory))

    def test_ServiceModel(self):
        category = ServiceCategory.objects.create(categoryName='Beauty')
        category.save()
        service = Service.objects.create(service_name='Daniel', service_category=category)
        self.assertEquals(str(service),"Daniel|Beauty")