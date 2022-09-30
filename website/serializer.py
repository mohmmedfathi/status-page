from gettext import install
from drf_writable_nested import WritableNestedModelSerializer
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
    

class WebsiteSerializer(WritableNestedModelSerializer):
    pages = PageSerializer(many = True,  allow_null = True,allow_empty = True, required=False, source='page_set')
    class Meta:
        model = Website
        fields = "__all__"
    # def create(self, validated_data):  
    #     print(validated_data.get('pages')) # None
    #     print('*' *50);
    #     print(validated_data)
    #     if 'pages' in validated_data:
    #         print('yes')
    #         pages_data = validated_data.pop('pages')
    #         lst = []
    #         wwebsite = Website.objects.create(**validated_data)
    #         #lst.extend(wwebsite)
    #         for page_data in pages_data:
    #             print('yes in loop')
    #             x = Page.objects.create(website=wwebsite, **page_data)
    #          #   lst.extend(x)
    #         return wwebsite
    #     else:
    #      website = Website.objects.create(
    #        **validated_data
    #     )
    #      return website

    # def create(self, validated_data):
    #  if 'pages' in validated_data:
    #     page_data = validated_data.pop('pages')
    #     print(page_data)
    #     website = Website.objects.create(
    #         page = Page.objects.create(
    #             **page_data
    #         )
    #        **validated_data
    #     )
    #     print(website)
    #     return website
    #  else:
    #   website = Website.objects.create(
    #        **validated_data
    #     )
    #  return website
        # 1 - validate page
        # 2 - create website
        # 3 - create page