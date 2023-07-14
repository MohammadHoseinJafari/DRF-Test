from django.shortcuts import render
from .models import Customer
from django.shortcuts import *
from .serializers import CustomerSerializers
from rest_framework import generics

# Create your views here.
def home(request):
    return render(request,'home/main.html')

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
