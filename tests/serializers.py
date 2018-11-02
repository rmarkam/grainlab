from rest_framework import serializers
from .models import GrainTest


class GrainTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrainTest
        fields = ("id", "test_id", "grain_type", "quantity", "unit", "infestation_days", "supplier_name", "supplier_country", "supplier_region", "supplier_city", "supplier_zip", "buyer_name", "buyer_country", "buyer_region", "buyer_city", "buyer_zip", "notes", "date", "time")