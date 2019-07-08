from django.shortcuts import render
from .models import *

# Create your views here.
def FormPage(request):
    return render(request,"app/registration.html")
def RegisterUser(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    pwd=request.POST['pwd']

    newuser= User.objects.create(fname=fname,lname=lname,email=email,pwd=pwd)
    return render(request,"app/success.html")
