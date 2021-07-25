from django.contrib import admin
from django.urls import path
from .views import index, signup,login

urlpatterns =[
    path('', index, name="index" ),
    path('signup', signup),
     path('login', login)
]