import json
from django.http import HttpResponse
from doctor.models import doctors
from medera.models import patient
from doctor.models import appoint
from receptionist.models import reclogin
from django.core import serializers
# Create your views here.


def login(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        print(body)
        x=reclogin.objects.filter(user=body['user'],pass1=body['pass1'])
        if(not x.exists()):
            print("Wrong username or password")
            return HttpResponse("Wrong username or password",status=401)
        else:
            print("Success")
            return HttpResponse("Success",status=200)


def appointments(request):
    if(request.method=="POST"):
        x=appoint.objects.filter(appoint='pending')
        data=serializers.serialize('json',x)
        print(data)
        return HttpResponse(data,content_type='application/json')


def payment(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        print(body)
        x=appoint.objects.filter(user=body['user'], appointment=body['appoint'], appoint='booked')[0]
        x.pay='paid'
        x.save()
        return HttpResponse("Success",status=200)


def approveappoint(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        data = appoint.objects.get(
            user=body['user'], appointment=body['appointment'], doctor=body['doctor'])
        data.appoint='dpending'
        data.save()
        return HttpResponse('Success', status=200)


def dynamic1(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        data=doctors.objects.filter(gender=body['gender'])
        #data=serializers.serialize('json',data)
        x=[]
        for i in data:
            d={'user':i.user, 'fname':i.fname, 'lname':i.lname, 'mail':i.mail, 'phone':i.phone}
            x.append(d)
        print(x)
        return HttpResponse(json.dumps(x),status=200)


def dynamic2(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        data=appoint.objects.filter(doctor=body['doctor'])
        x=[]
        for i in data:
            d={'user':i.user}
            x.append(d)
        return HttpResponse(json.dumps(x),status=200)


def allpatient(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        data=patient.objects.filter(gender=body['gender'])
        x=[]
        for i in data:
            d={'user':i.user,'fname':i.fname, 'lname':i.lname, 'mail':i.mail, 'phone':i.phone}
            x.append(d)
        return HttpResponse(json.dumps(x),status=200)