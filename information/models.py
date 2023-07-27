from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.db import IntegrityError
# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser as True"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active as True"))

        return self.create_user(email,password,**extra_fields)


class Information(AbstractUser):
    USER_TYPE = ((1,'"HOD',2,"Staff"))


    user_type = models.CharField(default=1,choices=USER_TYPE,max_length=1)
    STATUS = [('ACTIVE','ACTIVE'),('RETIRED','RETIRED'),('RESIGNED','RESIGNED'),('OTHERS','OTHERS')]
    GENDER = (('MALE','M'),('FEMALE','F'))
    LOCAL_GOVERNMENT = (('Agege Local Government','Agege Local Government'),('Ajeromi-Ifelodun Local Government','Ajeromi-Ifelodun Local Government'),('Alimosho Local Government','Alimosho Local Government'),('Amuwo-Odofin Local Government','Amuwo-Odofin Local Government'),
    ('Apapa Local Government','Apapa Local Government'),('Badagry Local Government','Badagry Local Government'),('Epe Local Government','Epe Local Government'),('Eti-Osa Local Government','Eti-Osa Local Government'),('Ibeju-Lekki Local Government','Ibeju-Lekki Local Government'),('Ifako-Ijaiye Local Government','Ifako-Ijaiye Local Government'),('Ikeja Local Government','Ikeja Local Government'),('Ikorodu Local Government','Ikorodu Local Government'),('Kosofe Local Government','Kosofe Local Government','Lagos Island Local Government','Lagos Island Local Government'),('Lagos Mainland Local Government','Lagos Mainland Local Government'),('Mushin Local Government','Mushin Local Government'),('Ojo Local Government','Ojo Local Government'),('Oshodi-Isolo Local Government','Oshodi-Isolo Local Government'),('Shomolu Local Government','Shomolu Local Government'),('Surulere Local Government','Surulere Local Government'),('outside Nigeria','outside Nigeria'))
    GRADE = (('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17'))
    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=5,choices=GRADE,null=False)
    gender = models.CharField(max_length=6,choices=GENDER,null=False,default='MALE')
    qualification = models.CharField(max_length=60)
    date_birth = models.DateField()
    state_origin = models.CharField(max_length=50,choices=LOCAL_GOVERNMENT)
    designation_appointement = models.CharField()
    date_first_appointment = models.DateField()
    date_present_appointment = models.DateField()
    employee_number = models.CharField(max_length=20)
    civil_service_number = models.CharField(max_length=20)
    mepb_file_number = models.CharField(max_length=20)
    present_post = models.CharField(max_length=20)
    mdas_posted = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    phone_num_nextofkin = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='images/',null=True,blank=True)
    description = models.CharField(max_length=3000)
    status = models.CharField(max_length=20,choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



class Admin(models.Model):
    admin = models.OneToOneField(Information,on_delete=models.CASCADE)




class Department(models.Model):
    admin = models.OneToOneField(Information,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Designation(models.Model):
    admin = models.OneToOneField(Information,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    start_year = models.DateField()
    end_year = models.DateField()
    def __str__(self):
        return "from" + str(self.start_year) + "to" + str(self.end_year)

class Staff(models.Model):
    admin = models.OneToOneField(Information,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    


 


    
    
