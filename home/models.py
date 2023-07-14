from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length = 255 )
    location = models.CharField(max_length = 255 )
    job_title = models.CharField(max_length = 255 )
    last = models.IntegerField()
    applicant = models.IntegerField()
    job_site = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255)
    req = models.CharField(max_length=255)
    des = models.TextField(max_length=255)
    phone = models.CharField(max_length = 255 )
    Email = models.EmailField()

    def __str__(self):
        return self.job_title