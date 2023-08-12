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




class Testinga(generics.GenericAPIView):
    queryset = Texta.objects.all()
    serializer_class = serializers.TestingSerializer
    permission_class = [IsAdminUser]
    def get(self,request):
        users = Texta.objects.all()
        serializers = self.serializer_class(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)





class Testingb(generics.GenericAPIView):
    queryset = Textb.objects.all()
    serializer_class = serializers.TestingbSerializer
    permission_class = [IsAdminUser]
    def get(self,request):
        users = Textb.objects.all()
        serializers = self.serializer_class(users,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            # validated_data = serializers.validated_data
            # validated_data.pop('name')
            # instance = Textb.objects.create(**validated_data)
            # serializers.save(validated_data)
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)










# class Testingb(generics.GenericAPIView):
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#         # Remove the inherited name field before saving
#             validated_data = serializer.validated_data
#             validated_data.pop('name', None)
        
#             instance = Textb.objects.create(**validated_data)
#             return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self,request):
#         users = Textb.objects.all()
#         serializers = self.serializer_class(users,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)
#     # def post(self,request):
#     #     serializers = self.serializer_class(data=request.data)
#     #     if serializers.is_valid():
#     #         serializers.save()     
#     #         return Response(serializers.data,status=status.HTTP_200_OK)
#     #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# # class Testingb(generics.GenericAPIView):
# #     serializer_class = serializers.TestingbSerializer  # Make sure to define this attribute
    
# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             validated_data = serializer.validated_data
# #             validated_data.pop('name', None)
        
# #             instance = Textb.objects.create(**validated_data)
# #             return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #     def get(self, request):
# #         users = Textb.objects.all()
# #         serializer = self.serializer_class(users, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)


# # class Testingb(generics.ListCreateAPIView):
# #     queryset = Textb.objects.all()  # Define the queryset attribute
# #     serializer_class = serializers.TestingbSerializer
# #     permission_classes = [IsAdminUser]

# #     def post(self, request, *args, **kwargs):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             validated_data = serializer.validated_data
# #             instance = Textb.objects.create(**validated_data)
# #             return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #     def get(self, request, *args, **kwargs):
# #         queryset = self.get_queryset()  # Use the queryset attribute
# #         serializer = self.serializer_class(queryset, many=True)
# #         return Response(serializer.data, status=status.HTTP_200_OK)



# # class Testingb(generics.GenericAPIView):
# #     # queryset = Textb.objects.all()  # Define the queryset attribute
# #     # serializer_class = serializers.TestingbSerializer
# #     # permission_classes = [IsAdminUser]

# #     def post(self, request):
# #         serializer = self.serializer_class(data=request.data)
# #         if serializer.is_valid():
# #             # validated_data = serializer.validated_data
# #             # validated_data.pop('name', None)  # Remove the 'name' field
# #             instance = Textb.objects.create(**validated_data)
# #             return Response(self.serializer_class(instance).data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #     # def get(self, request):
# #     #     queryset = Textb.objects.all()
# #     #     serializer = self.serializer_class(queryset, many=True)
# #     #     return Response(serializer.data, status=status.HTTP_200_OK)





