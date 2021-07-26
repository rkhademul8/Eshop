from django.contrib import admin
from django.urls import path
from .views import  Signup,Login, Index

urlpatterns =[
    path('', Index.as_view(), name="index" ),
    path('signup', Signup.as_view(), name='signup'),
     path('login', Login.as_view(), name='login'),
]