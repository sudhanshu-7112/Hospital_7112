from django.db import models

# Create your models here.

class patient(models.Model):
    fname=models.CharField(max_length=25, null=False, blank=False)
    lname=models.CharField(max_length=25, null=False, blank=False)
    mail=models.EmailField(max_length=50, null=False, blank=False)
    phone=models.BigIntegerField(null=False, blank=False)
    doctor=models.CharField(max_length=50, null=False, blank=False)
    user=models.CharField(max_length=25, primary_key=True)
    pass1=models.CharField(max_length=100, null=False, blank=False)

class doctors(models.Model):
    fname=models.CharField(max_length=25, null=False, blank=False)
    lname=models.CharField(max_length=25, null=False, blank=False)
    mail=models.EmailField(max_length=50, null=False, blank=False)
    phone=models.BigIntegerField(null=False, blank=False)
    user=models.CharField(max_length=25, primary_key=True)
    college=models.CharField(max_length=25, null=False, blank=False)
    degree=models.CharField(max_length=10, null=False, blank=False)
    cgpa=models.IntegerField(null=False, blank=False)
    pass1=models.CharField(max_length=100, null=True, blank=True)