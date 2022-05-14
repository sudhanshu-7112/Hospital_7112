from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('d-register',views.dreg),
    path('d-login',views.dlog)
]