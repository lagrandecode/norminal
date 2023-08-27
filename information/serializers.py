from rest_framework import serializers
from .models import *
from datetime import datetime





class UserCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    password = serializers.CharField(max_length=18,write_only=True)
    class Meta:
        model = User
        fields = ['email','password']


# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
    def get_department_text(self,obj):
        try:
            department.objects.get(pk=obj.department)

        except Department.DoesNotExist:
            return None





class DesignationSerializer(serializers.ModelSerializer):
    def _get_designation(self,obj):
        return obj.designation.name
    class Meta:
        model = Designation
        fields = '__all__'




# class DesignationSerializer(serializers.ModelSerializer):
#     designation_name = serializers.SerializerMethodField()

#     def get_designation_name(self, obj):
#         return obj.name

#     class Meta:
#         model = Designation
#         fields = '__all__'













































# # class InformationSerializer(serializers.ModelSerializer):

# #     LOCAL_GOVERNMENT = (
# #     ('Agege Local Government', 'Agege Local Government'),
# #     ('Ajeromi-Ifelodun Local Government', 'Ajeromi-Ifelodun Local Government'),
# #     ('Alimosho Local Government', 'Alimosho Local Government'),
# #     ('Amuwo-Odofin Local Government', 'Amuwo-Odofin Local Government'),
# #     ('Apapa Local Government', 'Apapa Local Government'),
# #     ('Badagry Local Government', 'Badagry Local Government'),
# #     ('Epe Local Government', 'Epe Local Government'),
# #     ('Eti-Osa Local Government', 'Eti-Osa Local Government'),
# #     ('Ibeju-Lekki Local Government', 'Ibeju-Lekki Local Government'),
# #     ('Ifako-Ijaiye Local Government', 'Ifako-Ijaiye Local Government'),
# #     ('Ikeja Local Government', 'Ikeja Local Government'),
# #     ('Ikorodu Local Government', 'Ikorodu Local Government'),
# #     ('Kosofe Local Government', 'Kosofe Local Government'),
# #     ('Lagos Island Local Government', 'Lagos Island Local Government'),
# #     ('Lagos Mainland Local Government', 'Lagos Mainland Local Government'),
# #     ('Mushin Local Government', 'Mushin Local Government'),
# #     ('Ojo Local Government', 'Ojo Local Government'),
# #     ('Oshodi-Isolo Local Government', 'Oshodi-Isolo Local Government'),
# #     ('Shomolu Local Government', 'Shomolu Local Government'),
# #     ('Surulere Local Government', 'Surulere Local Government'),
# #     ('other state in Nigeria','other state in Nigeria'),
# #     ('Outside Nigeria', 'Outside Nigeria'),)

# #     STATUS = [('ACTIVE','ACTIVE'),('RETIRED','RETIRED'),('RESIGNED','RESIGNED'),('OTHERS','OTHERS')]

# #     email = serializers.EmailField(max_length=80)
# #     surname = serializers.CharField(max_length=200)
# #     name = serializers.CharField(max_length=200)
# #     other_name = serializers.CharField(max_length=200)
# #     grade_level = serializers.ChoiceField(choices=[('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17')])
# #     gender = serializers.ChoiceField(choices=[('M','MALE'),('F','FEMALE')])
# #     qualification = serializers.CharField(max_length=60)
# #     date_birth = serializers.DateField(default=datetime.now)
# #     state_origin = serializers.ChoiceField(choices=LOCAL_GOVERNMENT)
# #     designation_appointement = serializers.CharField(max_length=150)
# #     date_first_appointment = serializers.DateField(default=datetime.now)
# #     date_present_appointment = serializers.DateField(default=datetime.now)
# #     employee_number = serializers.CharField(max_length=20)
# #     civil_service_number = serializers.CharField(max_length=20)
# #     mepb_file_number = serializers.CharField(max_length=20)
# #     present_post = serializers.CharField(max_length=500)
# #     mdas_posted = serializers.CharField(max_length=150)
# #     phone_number = serializers.CharField(max_length=20)
# #     phone_num_nextofkin = serializers.CharField(max_length=20)
# #     profile_pic = serializers.ImageField()
# #     biography = serializers.CharField(max_length=5000)
# #     status = serializers.ChoiceField(choices=STATUS)
# #     department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
# #     designation = serializers.PrimaryKeyRelatedField(queryset=Designation.objects.all())

# #     class Meta:
# #         model = User
# #         fields = ['name',
# #         'other_name',
# #         'surname',
# #         'email',
# #         'grade_level',
# #         'gender',
# #         'qualification',
# #         'date_birth',
# #         'state_origin',
# #         'designation_appointement',
# #         'date_first_appointment',
# #         'date_present_appointment',
# #         'employee_number',
# #         'civil_service_number',
# #         'mepb_file_number',
# #         'present_post',
# #         'mdas_posted',
# #         'phone_number',
# #         'phone_num_nextofkin',
# #         'profile_pic',
# #         'biography',
# #         'status',
# #         'department',
# #         'designation',
# #         ]






        

# class StaffSerializer(InformationSerializer):
#     couse = UserCreationSerializer(many=True,write_only=True)
#     class Meta(InformationSerializer.Meta):
#         model = Staff
#         fields = InformationSerializer.Meta.fields + ['course']

# class StaffSerializer(serializers.ModelSerializer):
#     course = UserCreationSerializer(many=True,write_only=True)
#     class Meta:
#         model = Staff
#         fields = '__all__'


#     # def create(self,validated_data):
#     #     course_data=validated_data.pop('course')
#     #     author = Staff.objects.create(**validated_data)

#     #     for course_datas in course_data:







# # class BookSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Book
# #         fields = '__all__'

# # class AuthorSerializer(serializers.ModelSerializer):
# #     books = BookSerializer(many=True, write_only=True)  # To write nested books

# #     class Meta:
# #         model = Author
# #         fields = '__all__'

# #     def create(self, validated_data):
# #         books_data = validated_data.pop('books')
# #         author = Author.objects.create(**validated_data)

# #         for book_data in books_data:
# #             Book.objects.create(author=author, **book_data)

# #         return author




