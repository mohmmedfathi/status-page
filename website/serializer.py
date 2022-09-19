from gettext import install
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Website,Page,PageHistory



class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = "__all__"
        


class PageHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PageHistory
        fields = "__all__"
    

class WebsiteSerializer(serializers.ModelSerializer):
    #page = PageSerializer(many = True, allow_null = True,allow_empty = True, required=False)
    page = PageSerializer(many = True,allow_null = True,allow_empty = True, required=False)
    class Meta:
        model = Website
        fields = "__all__"
    
    def create(self, validated_data):
     if 'page' in validated_data:
        page_data = validated_data.pop('page')
        website = Website.objects.create(
            page = Page.objects.create(
                **page_data
            )
           **validated_data
        )
        return website
     else:
      website = Website.objects.create(
           **validated_data
        )
     return website
        # 1 - validate page
        # 2 - create website
        # 3 - create page