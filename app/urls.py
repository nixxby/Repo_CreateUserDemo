from django.urls import path,include
from . import views
urlpatterns = [

    path("",views.FormPage,name="form"),
    path("registeruser/",views.RegisterUser,name="registeruser"),

]