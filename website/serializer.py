from rest_framework import serializers
from .models import Website,Page,Page_status_history

class WebsiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Website
        fields = "__all__"


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = "__all__"
        


class PageStatusHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Page_status_history
        fields = "__all__"
    
    