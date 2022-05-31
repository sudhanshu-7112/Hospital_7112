import hashlib
import json
import re
from reportlab.pdfgen import canvas
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from doctor.models import doctors
from medera.models import patient
from doctor.models import appoint, patientrecord

# Create your views here.


def register(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        x = patient.objects.filter(user=body['user'])
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
        if(body['phone'] < 1000000000 or body['phone'] > 9999999999):
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
        r = patient.objects.create(fname=body['fname'], lname=body['lname'],
                                   mail=body['mail'], phone=body['phone'], gender=body['gender'], user=body['user'], pass1=p)
        print("Success account created")
        patientrecord.objects.create(user=r)
        return HttpResponse("Success account created", status=201)


def login(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        p = body['pass1']
        p = (hashlib.md5(p.encode())).hexdigest()
        x = patient.objects.filter(user=body['user'], pass1=p)
        if(not x.exists()):
            return HttpResponse("Wrong username or password", status=401)
        else:
            request.session['id']=x[0].user
            return HttpResponse("success", status=200)


def phome(request):
    body = json.loads(request.body)
    print(body)
    #if(request.session['id']!=body['user'] or request.session['id']==None):
     #    return HttpResponse("Error",status=403)
    x = patient.objects.get(user=body['user'])
    x=model_to_dict(x)
    return JsonResponse(x, safe=False, status=200)


def appointment(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user']):
        #     return HttpResponse("Error",status=403)
        y = doctors.objects.get(user=body['doctor'])
        x = patient.objects.get(user=body['user'])
        z = appoint(user=x, doctor=y, appointment=body['appointment'])
        z.save()
        return HttpResponse("Success")


def mhistory(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user']):
        #     return HttpResponse("Error",status=403)
        x=patient.objects.get(user=body['user'])
        y=list(patientrecord.objects.filter(user=x).values())
        # response=HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="medical_history.pdf"'
        # p = canvas.Canvas(response)
        # p.drawString(100,100,str(y))
        # p.showPage()
        # p.save()
        # return response
        return JsonResponse(y,safe=False, status=200)


def prescription(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user']):
        #     return HttpResponse("Error",status=403)
        x=patient.objects.get(user=body['user'])
        y=appoint.objects.filter(user=x)
        y=list(patientrecord.objects.filter(user=x).values())
        # response=HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="medical_history.pdf"'
        # p = canvas.Canvas(response)
        # p.drawString(100,100,str(y))
        # p.showPage()
        # p.save()
        # return response
        return JsonResponse(y,safe=False, status=200)


def pay(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        # if(request.session['id']!=body['user']):
        #     return HttpResponse("Error",status=403)
        x=list(appoint.objects.filter(pay='pending', user=body['user']).values())
        return JsonResponse(x,safe=False, status=200)


def logout(request):
    if(request.method == "POST"):
        body = json.loads(request.body)
        print(body)
        del request.session['id']
        return HttpResponse("Logout Succesfully")