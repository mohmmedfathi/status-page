from operator import imod
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Website,PageHistory
from .models import Page as PageModel
from .serializer import PageHistorySerializer, PageSerializer, WebsiteSerializer,PageHistory
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.authentication import TokenAuthentication
from django.core.paginator import Paginator
from .permission import IsUser
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class Website(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']




class Page(ModelViewSet):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsUser]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['Page']

class PageHistoryViewSet(ModelViewSet):
    queryset = PageHistory.objects.all()
    serializer_class = PageHistorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Page', 'Page__website']

    

class checkWebsiteNow(APIView):
    def get(self, request,pk): 
        x = PageModel.objects.filter(id = pk).first()
       
        if x is not None:
            response = requests.get(url = x.url) 
            PageHistory.objects.create(
                     Page = x,
                     satus_code = response.status_code,
                     text = response.text,
                     headers = response.headers,
                     response_time = response.elapsed.total_seconds()
         )
            serializer = PageHistorySerializer(PageHistory.objects.latest('id'))
            
            return Response(serializer.data)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
