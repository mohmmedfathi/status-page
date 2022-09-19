"""statuspage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include


from rest_framework.authtoken import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('',include('website.urls')),
   

   # path('website/<int:pk>',WebsiteRetrieve.as_view()),

  #  path('page/<int:pk>',PageRetrieve.as_view()),
   #  path("", include("request_automation_request.urls", namespace="main"))

    #path('page-history/<int:pk>',PageStatusHistoryRetrieve.as_view()),
]

