import re
from rest_framework import permissions
from .models import Website,Page,PageHistory
class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if isinstance(obj, Website) == True:
            return obj.user == request.user
            
        elif isinstance(obj, Page) == True:
            return obj.website.user == request.user

        elif isinstance(obj, PageHistory) == True:
            return obj.page.website.user == request.user
        