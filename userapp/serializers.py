from rest_framework import serializers
from userapp.models import Flatmate
from userapp.models import Room
from django.contrib.auth.models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    extra_kwargs = {
        'first_name': {'required': True, 'allow_blank': False},
        'last_name': {'required': True, 'allow_blank': False},
        'email': {'required': True, 'allow_blank': False},
        'password': {'required': True, 'allow_blank': False},      
    }    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username')

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class FlatmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flatmate
        fields = '__all__'        