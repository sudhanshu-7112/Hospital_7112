from django.db import models


# Create your models here.

class patient(models.Model):
    fname=models.CharField(max_length=25, null=False, blank=False)
    lname=models.CharField(max_length=25, null=False, blank=False)
    mail=models.EmailField(max_length=50, null=False, blank=False)
    phone=models.BigIntegerField(null=False, blank=False)
    gender=models.CharField(max_length=6, default='Male')
    user=models.CharField(max_length=25, primary_key=True)
    pass1=models.CharField(max_length=100, null=False, blank=False)

class patientrecord(models.Model):
    user=models.ForeignKey(patient, on_delete=models.CASCADE)
    mhistory=models.CharField(max_length=100, null=True)
    prescription=models.CharField(max_length=100, null=True)

