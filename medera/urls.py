from django.urls import path
from medera import views

urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('appointment',views.appointment),
    path('home', views.phome)
    
]