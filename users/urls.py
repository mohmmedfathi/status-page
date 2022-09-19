from django.urls import path, include
from . import api 
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .api import viewsets_user
from rest_framework.authtoken import views


route = DefaultRouter()
#route.register(r'user', viewsets_user)

urlpatterns = [
    path('', include(route.urls)),

    path('token/',views.obtain_auth_token),
    
    # path('user/',viewsets_user.as_view({'post': 'create',
    #                                     'get':'list'})),
    path('user/',viewsets_user.as_view({'post': 'create'})),
]
