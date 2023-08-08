from django.shortcuts import render
from rest_framework import status,generics 
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from .models import *
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.



class SignupView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserCreationSerializer
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            if request.user.user_type == '1':
                return Response({'message':'admin page'})
            if request.user.user_type == '2':
                return Response({'message':"staff user interface"})


class UserInfo(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.InformationSerializer
    permission_class = [IsAdminUser]
    def get(self,request):

        users = User.objects.all()
        serializers = self.serializer_class(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



class StaffInfo(generics.GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_class = [IsAdminUser]
    def get(self,request):

        users = Staff.objects.all()
        serializers = self.serializer_class(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

