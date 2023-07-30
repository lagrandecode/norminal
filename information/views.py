from django.shortcuts import render
from rest_framework import status,generics 
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from .models import *
from . import serializers

# Create your views here.



class SignupView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response



class LoginView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.user_type == '1':
                return Response({'message':'admin page'})
            if request.user.user_type == '2':
                return Response({'message':"staff user interface"})

