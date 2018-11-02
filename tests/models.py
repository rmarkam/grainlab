from django.db import models
from random import randint
import uuid
            
class GrainTest(models.Model):
    test_id = models.CharField(max_length=255, default=uuid.uuid4)
    grain_type = models.CharField(max_length=255, null=False)
    quantity = models.CharField(max_length=255, null=False)
    infestation_days= models.IntegerField(default=randint(1,30))
    unit = models.CharField(max_length=255, null=False, default='kg')
    supplier_name = models.CharField(max_length=255, null=False)
    supplier_country = models.CharField(max_length=255, null=False)
    supplier_region = models.CharField(max_length=255, null=False)
    supplier_city = models.CharField(max_length=255, null=False)
    supplier_zip = models.CharField(max_length=255, null=False)
    buyer_name = models.CharField(max_length=255, null=False)
    buyer_country = models.CharField(max_length=255, null=False)
    buyer_region = models.CharField(max_length=255, null=False)
    buyer_city = models.CharField(max_length=255, null=False)
    buyer_zip = models.CharField(max_length=255, null=False)
    notes = models.TextField(max_length=255)
    sample_image = models.ImageField()
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
