import hashlib
import json
import re
from django.http import HttpResponse
from django.core import serializers
from doctor.models import doctors, appoint, patientrecord
from medera.models import patient

# Create your views here.


def register(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
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
            return HttpResponse("Error atleast 1 special character should be there in password", status=401)
        if(body['pass1'] != body['pass2']):
            print("Error password doesn't matched")
            return HttpResponse("Error password doesn't matched", status=401)
        p = body['pass1']
        p = (hashlib.md5(p.encode())).hexdigest()
        doctors.objects.create(fname=body['fname'], lname=body['lname'], college=body['college'], gender=body['gender'], degree=body['degree'],
                               mail=body['mail'], phone=body['phone'], dob=body['dob'], user=body['user'], pass1=p)
        print("Success account created")
        return HttpResponse("Success account created", status=201)


def login(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        p = body['pass1']
        p = (hashlib.md5(p.encode())).hexdigest()
        x = doctors.objects.filter(user=body['user'], pass1=p)
        if(not x.exists()):
            print("Wrong username or password")
            return HttpResponse("Wrong username or password", status=401)
        else:
            data = doctors.objects.get(user=body['user'])
            data = {'user': data.user}
            return HttpResponse(json.dumps(data), status=201)


def getdoctor(request):
    if(request.method == "POST"):
        x = doctors.objects.all()
        d=[]
        for i in x:
            s={'user':i.user}
            d.append(s)
        return HttpResponse(json.dumps(d), status=200)


def getpatient(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        x = appoint.objects.filter(doctor=body['doctor'])
        data = serializers.serialize('json', x)
        # data={'user':x[0].user}
        return HttpResponse(data, content_type='application/json', status=200)


def doctordetail(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = doctors.objects.get(user=body['user'])
        x = {'fname': data.fname, 'lname': data.lname, 'mail': data.mail, 'degree': data.degree,
             'phone': data.phone, 'college': data.college, 'gender': data.gender, 'user': data.user}
        return HttpResponse(json.dumps(x), status=200)


def updatehistory(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = patientrecord.objects.get(user=body['user'])
        data.mhistory = body['mhistory']
        data.save()
        return HttpResponse('Success', status=200)


def updateprescription(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = patientrecord.objects.get(user=body['user'])
        data.prescription = body['prescription']
        data.save()
        return HttpResponse('Success', status=200)


def addappointment(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        x = patient.objects.get(user=body['user'])
        y = doctors.objects.get(user=body['doctor'])
        appoint.objects.create(
            user=x, doctor=y, appointment=body['appointment'], appoint='booked', pay='pending')
        return HttpResponse('Success', status=200)


def delappointment(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = appoint.objects.get(
            user=body['user'], appointment=body['appointment'], doctor=body['doctor'])
        data.delete()
        return HttpResponse('Success', status=200)


def updateappointment(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = appoint.objects.filter(
            user=body['user'], appointment=body['appointment'], doctor=body['doctor'],appoint='booked')
        data.appointment = body['newappoint']
        data.appoint = 'booked'
        data.pay = 'pending'
        data[0].save()
        return HttpResponse('Success', status=200)


def pending(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        a = appoint.objects.filter(doctor=body['user'], appoint='dpending')
        a = serializers.serialize('json', a)
        return HttpResponse(a, content_type='application/json')


def booked(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        a = appoint.objects.filter(
            doctor=body['user'], appoint='booked')
        a = serializers.serialize('json', a)
        return HttpResponse(a, content_type='application/json')


def approveappoint(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        data = appoint.objects.get(
            user=body['user'], appointment=body['appointment'], doctor=body['doctor'])
        data.appoint='booked'
        data.pay='pending'
        data.save()
        return HttpResponse('Success', status=200)
