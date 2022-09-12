from operator import imod
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Website,Page,Page_status_history
from .serializer import PageSerializer, WebsiteSerializer,PageStatusHistorySerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.authentication import TokenAuthentication
from django.core.paginator import Paginator
# Create your views here.
class Website(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
"""
class WebsiteRetrieve(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
"""

class Page(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
"""
class PageRetrieve(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
"""

# class PageStatusHistory(ModelViewSet):
#     queryset = Page_status_history.objects.all()
#     serializer_class = PageStatusHistorySerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
   
class PageStatusHistory(ModelViewSet):
    queryset = Page_status_history.objects.all()
    serializer_class = PageStatusHistorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

