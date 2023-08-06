from rest_framework import serializers
from .models import *




class InformationSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(max_length=80)
    # password = serializers.CharField(max_length=18,write_only=True)
    class Meta:
        model = User
        fields = '__all__'


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(max_length=18,write_only=True)
    class Meta:
        model = User
        fields = ['email','password']