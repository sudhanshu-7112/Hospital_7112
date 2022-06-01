import json
from django.http import HttpResponse, JsonResponse
from doctor.models import doctors
from medera.models import patient
from doctor.models import appoint
from receptionist.models import reclogin
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
            request.session['id']=x[0].user
            return HttpResponse("Success",status=200)


def appointments(request):
    if(request.method=="POST"):
        body = json.loads(request.body)
        #if(request.session['id']!=body['user'] or request.session['id']==None):
        #    return HttpResponse("Error",status=403)
        x=list(appoint.objects.filter(appoint='pending', delete=0).values())
        print(x)
        return JsonResponse(x, safe=False)


def payment(request):
    if(request.method=="POST"):
        body=json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user'] or request.session['id']==None):
        #     return HttpResponse("Error",status=403)
        x=appoint.objects.get(id=body['id'])
        x.pay='paid'
        x.save()
        return HttpResponse("Success",status=200)


def approveappoint(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user'] or request.session['id']==None):
        #     return HttpResponse("Error",status=403)
        data = appoint.objects.get(id=body['id'])
        data.appoint='dpending'
        data.save()
        return HttpResponse('Success', status=200)


def dynamic1(request):
    if(request.method == "POST"):
        # if(request.session['id']!=body['user'] or request.session['id']==None):
        #     return HttpResponse("Error",status=401)
        body = json.loads(request.body)
        data=list(doctors.objects.filter(gender=body['gender']).values())
        return JsonResponse(data, safe=False, status=200)


def dynamic2(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user'] or request.session['id']==None):
        #     return HttpResponse("Error",status=403)
        data=list(appoint.objects.filter(doctor=body['doctor']).values('user').distinct())
        print(data)
        return JsonResponse(data, safe=False, status=200)


def allpatient(request):
    if(request.method == "POST"):
        body=json.loads(request.body)
        # if(request.session['id']!=body['user'] or request.session['id']==None):
        #     return HttpResponse("Error",status=403)
        data=list(patient.objects.filter(gender=body['gender']).values())
        return JsonResponse(data, safe=False, status=200)


def logout(request):
    if(request.method == "POST"):
        #del request.session['id']
        return HttpResponse("Logout Succesfully")


def doctorname(request):
    if(request.method=="POST"):
        data=list(doctors.objects.all().values('user'))
        return JsonResponse(data, safe=False, status=200)