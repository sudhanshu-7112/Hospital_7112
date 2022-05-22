import datetime
import hashlib
import json
import re
from django.http import HttpResponse
from django.core import serializers

from doctor.models import doctors

# Create your views here.

def register(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(request.body)
        x = doctors.objects.filter(user=body['user'])
        if(x.exists()):
            print("Already exist user")
            return HttpResponse("Already exist user", status=401)
        if ((re.search("[0-9]", body['fname'].strip())) or body['fname'] == ""):
            print("Error not valid first name")
            return HttpResponse("Error not valid first name", status=401)
        if ((re.search("[0-9]", body['lname'].strip())) or body['lname'] == ""):
            print("Error not valid last name")
            return HttpResponse("Error not valid last name", status=401)
        if((not re.search("[a-zA-Z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}", body['mail'])) or body['mail'] == ""):
            print("Error invalid mail")
            return HttpResponse("Error invalid mail", status=401)
        if(body['phone'] < 100000000 or body['phone'] > 9999999999):
            print("Invalid phone number")
            return HttpResponse("Invalid Phone number", status=401)
        if(body['user'].strip() == ""):
            print("Invalid User")
            return HttpResponse("Invalid User", status=401)
        if(body['cgpa']>10):
            print("Invalid cgpa")
            return HttpResponse("Invalid cgpa", status=401)
        if(body['pass1'] == "" or body['pass2'] == ""):
            print("Error Enter Password")
            return HttpResponse("Error Enter Password", status=401)
        if(len(body['pass1']) < 8):
            print("Error password should be atleast 8 digits")
            return HttpResponse("Error password should be atleast 8 digits", status=401)
        if(not re.search("[0-9]", body['pass1'])):
            print("Error atleast 1 digit should be in password")
            return HttpResponse("Error atleast 1 digit should be in password", status=401)
        if(not re.search("[A-Z]", body['pass1'])):
            print("Error 1 Capital letter should be in password")
            return HttpResponse("Error 1 Capital letter should be in password", status=401)
        if(not re.search("[a-z]", body['pass1'])):
            print("Error 1 small letter should be in password")
            return HttpResponse("Error 1 small letter should be in password", status=401)
        if(not re.search("[@#$%&*]", body['pass1'])):
            print("Error atleast 1 special character should be there in password")
            return HttpResponse("Error atleast 1 special character should be there in password", status=404)
        if(body['pass1'] != body['pass2']):
            print("Error password doesn't matched")
            return HttpResponse("Error password doesn't matched", status=401)
        p = body['pass1']
        p = (hashlib.md5(p.encode())).hexdigest()
        doctors.objects.create(fname=body['fname'], lname=body['lname'], college=body['college'], cgpa=body['cgpa'], degree=body['degree'],
                                mail=body['mail'], phone=body['phone'], dob=body['dob'], user=body['user'], pass1=p)
        print("Success account created")
        return HttpResponse("Success account created", status=201)


def login(request):
    if(request.method=="POST"):
        body = json.loads(request.body)
        p = body['pass1']
        p = (hashlib.md5(p.encode())).hexdigest()
        x = doctors.objects.filter(user=body['user'], pass1=p)
        if(not x.exists()):
            print("Wrong username or password")
            return HttpResponse("Wrong username or password", status=401)
        else:
            print("Success")
            return HttpResponse("Success", status=201)


def getdoctor(request):
    if(request.method=="POST"):
        x=doctors.objects.all()
        data=serializers.serialize("json",x)
        return HttpResponse(data,content_type="application/json")