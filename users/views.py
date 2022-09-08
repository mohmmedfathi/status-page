import imp
from urllib import response
from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .authentication import TokenAuthentication
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # set up pagination
    pagination_class = PageNumberPagination

class Logout(GenericAPIView):
    def get(self, request, format=None):
        
        if request.is_authenticated():
            request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)

