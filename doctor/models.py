from django.db import models
from django.forms import BooleanField, IntegerField

# Create your models here.

class doctors(models.Model):
    fname=models.CharField(max_length=25, null=False, blank=False)
    lname=models.CharField(max_length=25, null=False, blank=False)
    mail=models.EmailField(max_length=50, null=False, blank=False)
    phone=models.BigIntegerField(null=False, blank=False)
    user=models.CharField(max_length=25, primary_key=True)
    dob=models.DateTimeField(null=True)
    college=models.CharField(max_length=25, null=False, blank=False)
    degree=models.CharField(max_length=10, null=False, blank=False)
    gender=models.CharField(max_length=6, default='Male')
    pass1=models.CharField(max_length=100, null=True, blank=True)

class appoint(models.Model):
    user=models.ForeignKey('medera.patient',on_delete=models.CASCADE)
    doctor=models.ForeignKey('doctor.doctors',on_delete=models.CASCADE)
    appointment=models.DateTimeField()
    appoint=models.CharField(max_length=12, default='pending')
    pay=models.CharField(max_length=12, default='not booked')
    delete=models.IntegerField(default=0)

class patientrecord(models.Model):
    user=models.ForeignKey('medera.patient', on_delete=models.CASCADE)
    mhistory=models.CharField(max_length=100, null=False, default='Nothing to Show')
    prescription=models.CharField(max_length=100, null=False, default='Nothing to show')

