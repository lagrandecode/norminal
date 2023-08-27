from django.shortcuts import render
from rest_framework import status,generics 
from rest_framework.response import Response 
from rest_framework.decorators import APIView
from .models import *
from . import serializers
from django.contrib.auth import authenticate, login
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



# class LoginView(APIView):
#     def get(self,request):
#         if request.user.is_authenticated:
#             if request.user.user_type == '1':
#                 return Response({'message':'admin page'})
#             if request.user.user_type == '2':
#                 return Response({'message':"staff user interface"})






# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
        
#         if user:
#             login(request, user)
            
#             if user.user_type == 1:
#                 admin_data = Admin.objects.all()
#                 # staff_data = {
#                 #     'user': user.id,
#                 #     'name': user.first_name + ' ' + user.last_name,
#                 #     'email': user.email,
#                 # }
#                 staff_serializer = StaffSerializer(data=admin_data)
#                 if staff_serializer.is_valid():
#                     staff_serializer.save()
#                     return Response({'message': 'Staff data saved successfully.'}, status=status.HTTP_200_OK)
#                 return Response(staff_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#             elif user.user_type == 2:
#                 staff_data = Staff.objects.all()
#                 # student_data = {
#                 #     'user': user.id,
#                 #     'name': user.first_name + ' ' + user.last_name,
#                 #     'email': user.email,
#                 #     'course': request.data.get('course'),
#                 # }
#                 student_serializer = StudentSerializer(data=staff_data)
#                 if student_serializer.is_valid():
#                     student_serializer.save()
#                     return Response({'message': 'Student data saved successfully.'}, status=status.HTTP_200_OK)
#                 return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#         return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)



class StaffInfo(generics.GenericAPIView):
    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_class = [IsAdminUser,]
    def get(self,request):
        ordering = request.query_params.get('created_at')
        users = Staff.objects.all().order_by(ordering)
        serializers = self.serializer_class(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


















# class UserInfo(generics.GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.InformationSerializer
#     permission_class = [IsAdminUser,]
#     def get(self,request):
#         permission_class = [IsAdminUser,]
#         users = User.objects.all()
#         serializers = self.serializer_class(users,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         permission_class = [IsAdminUser,]
#         serializers = self.serializer_class(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)














# class AuthorView(generics.GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = serializers.AuthorSerializer
#     permission_class = [IsAdminUser,]
#     def get(self,request):
#         permission_class = [IsAdminUser,]
#         users = Author.objects.all()
#         serializers = self.serializer_class(users,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         permission_class = [IsAdminUser,]
#         serializers = self.serializer_class(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        


# class BookView(generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = serializers.BookSerializer
#     permission_class = [IsAdminUser,]
#     def get(self,request):
#         permission_class = [IsAdminUser,]
#         users = Book.objects.all()
#         serializers = self.serializer_class(users,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         permission_class = [IsAdminUser,]
#         serializers = self.serializer_class(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        





