import imp
from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .authentication import TokenAuthentication
from django.core.paginator import Paginator
class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # set up pagination
    pagination_class = PageNumberPagination