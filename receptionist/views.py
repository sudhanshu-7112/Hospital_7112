import json
from django.http import HttpResponse, JsonResponse
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
        x=list(appoint.objects.filter(appoint='pending', delete=0).values())
        print(x)
        return JsonResponse(x, safe=False)


def payment(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        print(body)
        x=appoint.objects.get(user=body['user'], appointment=body['appoint'], appoint='booked')
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
        data=list(doctors.objects.filter(gender=body['gender']).values())
        return JsonResponse(data, safe=False, status=200)


def dynamic2(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        data=list(appoint.objects.filter(doctor=body['doctor']).values())
        return JsonResponse(data, safe=False, status=200)


def allpatient(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        data=list(patient.objects.filter(gender=body['gender']).values())
        return HttpResponse(data, safe=False, status=200)