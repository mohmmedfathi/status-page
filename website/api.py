from operator import imod
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Website,Page,PageHistory
from .serializer import PageSerializer, WebsiteSerializer,PageHistory
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.authentication import TokenAuthentication
from django.core.paginator import Paginator
from .permission import IsUser
from rest_framework.views import APIView
# Create your views here.

class Website(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsUser]

class Page(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsUser]
    

class PageHistoryViewSet(ModelViewSet):
    queryset = PageHistory.objects.all()
    serializer_class = PageHistory
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# class  PageRealTime(APIView):
#     def get(self, request,pk):
#         queryset = Page.objects.get(id = pk)
#         url_of_page = i.url
#         response = requests.get(url = url_of_page) 

#         PageHistory.objects.create(
#                      Page = i,
#                      satus_code = response.status_code,
#                      text = response.text,
#                      headers = response.headers,
#                      response_time = response.elapsed.total_seconds()
#          )