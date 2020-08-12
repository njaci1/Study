from django.conf.urls import url
from django.urls import include, path
from app_3 import views

app_name = 'app_3'

urlpatterns = [
    path('other/',views.other, name = 'other'),
    path('relative/',views.relative, name = 'relative'),
    path('',views.index, name='index')
]
