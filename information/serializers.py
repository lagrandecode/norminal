from rest_framework import serializers
from .models import *




class InformationSerializer(serializers.ModelSerializer):

    # email = serializers.EmailField(max_length=80)
    # password = serializers.CharField(max_length=18,write_only=True)
    class Meta:
        model = User
        fields = ['name','other_name','surname','email','grade_level','gender','qualification','date_birth','state_origin','designation_appointement','date_first_appointment',
        'date_present_appointment',
        'employee_number',
        'civil_service_number',
        'mepb_file_number',
        'present_post',
        'mdas_posted',
        'phone_number',
        'phone_num_nextofkin',
        'profile_pic',
        'description',
        'status',
        ]
        # fields = '__all__'


class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(max_length=18,write_only=True)
    class Meta:
        model = User
        fields = ['email','password']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'