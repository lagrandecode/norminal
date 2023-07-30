from django.shortcuts import render
from rest_framework import status,generics 
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from .models import *
from . import serializers

# Create your views here.



# class LoginView(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.InformationSerializer
#     def get(self,request):
#         user = User.objects.all()
#         serializers = serializer_class(user,many=True)
#         ret



class LoginView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.user_type == '1':
                return Response({'message':'admin page'})
            if request.user.user_type == '2':
                return Response({'message':"staff user interface"})

