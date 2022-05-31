from django.urls import path

from doctor import views

urlpatterns=[
    path('register',views.register),
    path('login',views.login),
    path('getdoctor',views.getdoctor),
    path('doctordetail',views.doctordetail),
    path('getpatient',views.getpatient),
    path('updatehistory',views.updatehistory),
    path('updateprescription',views.updateprescription),
    path('addappointment',views.addappointment),
    path('delappointment',views.delappointment),
    path('updateappointments',views.updateappointment),
    path('pending',views.pending),
    path('booked',views.booked),
    path('approve',views.approveappoint),
    path('logout',views.logout)

]