from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','password']
        extra_kwargs = {
            'password' : { 'write_only' : True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data['password']
        )
        return super().create(validated_data)

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password' : { 'write_only' : True}
        }
