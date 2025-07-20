from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from .models import * 
from .serializers import *
def home (request):
    return HttpResponse("Hello ")
# Create your views here.

def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products, many=True)
    return JsonResponse(serializer.data,safe=False)

def getCustomers(request):
    customers =Customer.objects.all()
    serial=CustomerSerializer(customers, many=True)
    return JsonResponse(serial.data,safe=False)



    


