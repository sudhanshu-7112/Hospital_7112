import json
from django.http import HttpResponse
from django.shortcuts import render
from medera.models import appoint
from receptionist.models import reclogin
from django.core import serializers
# Create your views here.


def login(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        x=reclogin.objects.filter(user=body['user'],pass1=body['pass1'])
        if(not x.exists()):
            print("Wrong username or password")
            return HttpResponse("Wrong username or password",status=401)
        else:
            print("Success",status=200)


def appointments(request):
    if(request.method=="POST"):
        x=appoint.objects.filter(appointdetails='pending')
        data=serializers.serialize('json',x)
        print(data)
        return HttpResponse(data,content_type='application/json')