from django.contrib import admin
from django.urls import path, include
from app_4 import views

app_name = 'app_4'

urlpatterns = [

        path('register/',views.register, name = 'register'),
        path('',views.index, name='index'),
        path('user_login/',views.user_login, name='user_login'),
]
