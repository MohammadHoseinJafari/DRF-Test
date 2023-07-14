from rest_framework import serializers
from .models import Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','company_name','location','job_title','last','applicant' ,'job_site' , 'job_type' , 'req' , 'des' , 'phone' , 'Email']

