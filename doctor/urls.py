from django.urls import path

from doctor import views

urlpatterns=[
    path('register',views.register),
    path('login',views.login),
    path('getdoctor',views.getdoctor)
]