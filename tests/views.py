from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GrainTest
from .serializers import GrainTestSerializer

def getResponseData(test: GrainTest):
    test_data = {
        "id": test.pk,
        "test_id": test.test_id,
        "grain_type": test.grain_type,
        "quantity": test.quantity,
        "unit": test.unit,
        "notes": test.notes,
        "good_grain_count": test.good_grain_count,
        "bad_grain_count": test.bad_grain_count,
        "total_grain_count": test.total_grain_count,
        "supplier_details": {
            "supplier_name": test.supplier_name,
            "supplier_country": test.supplier_country,
            "supplier_region": test.supplier_region,
            "supplier_city": test.supplier_city,
            "supplier_zip": test.supplier_zip
        }, 
        "buyer_details": {
            "buyer_name": test.buyer_name,
            "buyer_country": test.buyer_country,
            "buyer_region": test.buyer_region,
            "buyer_city": test.buyer_city,
            "buyer_zip": test.buyer_zip
        },
        "date": test.date,
        "time": test.time
    }
    return test_data

class TestsList(APIView):
    # Get all tests
    def get(self, request, format=None):
        retrieved = GrainTest.objects.all()
        tests = []
        for t in retrieved:
            test_data = getResponseData(t)
            tests.append(test_data)
        
        data = {
            "response": "true",
            "message": "All tests retrieved",
            "tests": tests  
        }

        return Response(data, status=status.HTTP_200_OK)

    


    # Submit new test
    def post(self, request, format=None):
        serializer = GrainTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            saved = GrainTest.objects.get(test_id=serializer.data['test_id'])
            data = {
            "response": "true",
            "message": "Test data submitted successfully.",
            "test_data": getResponseData(saved)  
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TestDetail(APIView):
    # Get a test by test_id
    def get(self, request, test_id, format=None):
        try:
            retrieved = GrainTest.objects.get(test_id=test_id)
            data = {
                "response": "true",
                "message": "Test with given id found",
                "test_data": getResponseData(retrieved)  
            }
            return Response(data, status=status.HTTP_200_OK)
        except GrainTest.DoesNotExist:
            raise Http404
        
    