from django.urls import path
from medera import views
from . import views

urlpatterns = [
    path('login',views.login),
    path('confirm',views.appointments),
    path('payment',views.payment),
    path('approve',views.approveappoint),
    path('d1',views.dynamic1),
    path('d2',views.dynamic2),
    path('allpatient',views.allpatient),
    path('logout',views.logout)
]