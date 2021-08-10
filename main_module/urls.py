from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('register2',views.registration2,name='register'),
    path('login_check',views.login_check,name='check'),
    path('get_report',views.getReport,name='report'),



]