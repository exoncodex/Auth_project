#urls here
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("",views.index,name="index")
]