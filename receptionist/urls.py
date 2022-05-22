from django.urls import path
from medera import views

urlpatterns = [
    path('login',views.login),
    path('confirm',views.appointment)
]