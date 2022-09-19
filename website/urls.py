from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import Website,Page,PageHistoryViewSet
route = DefaultRouter()

route.register(r'website',Website)
route.register(r'page',Page)
#route.register(r'page-history',PageStatusHistory)
# http://127.0.0.1:8000/page/<int:pk>/send/
urlpatterns = [
    path('', include(route.urls)),
    path('page-history/',PageHistoryViewSet.as_view({'get': 'list'})),
    #path('page-history/<int:id>/',PageHistory.as_view({'get': 'retrieve'})),
    # path('page/<int:pk>/send',)
]
