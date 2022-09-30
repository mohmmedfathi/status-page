import imp
from urllib import response
from django.contrib.auth.models import User
from rest_framework import generics, mixins, viewsets
from .serializer import UserSerializer,UserInfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from django.core.paginator import Paginator
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import GenericAPIView

class viewsets_user(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # set up pagination
    pagination_class = PageNumberPagination


class CurrentUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserInfoSerializer(instance=request.user)
        return Response(data=serializer.data)
