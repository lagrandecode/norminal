from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime

# from phonenumber_field.modelfields import PhoneNumberField

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


class User(AbstractUser):
    objects = MyUserManager()
    USER_TYPE = ((1,'"HOD',),(2,"Staff"))
    user_type = models.CharField(default=1,choices=USER_TYPE,max_length=1)
    email = models.EmailField(max_length=80,unique=True)
    username = None  # Removed username, using email instead
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []




class Department(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name

class Session(models.Model):
    start_year = models.DateField(null=False,blank=False,default=datetime.now)
    end_year = models.DateField(null=False,blank=False,default=datetime.now)
    def __str__(self):
        return "from" + str(self.start_year) + "to" + str(self.end_year)



# class Admin(models.Model):
#     admin = models.OneToOneField(User,on_delete=models.CASCADE)




class Staff(models.Model):
    # admin = models.OneToOneField(User,on_delete=models.CASCADE)
    STATUS = [('ACTIVE','ACTIVE'),('RETIRED','RETIRED'),('RESIGNED','RESIGNED'),('OTHERS','OTHERS')]
    GENDER = (('MALE','M'),('FEMALE','F'))
    LOCAL_GOVERNMENT = (
    ('Agege Local Government', 'Agege Local Government'),
    ('Ajeromi-Ifelodun Local Government', 'Ajeromi-Ifelodun Local Government'),
    ('Alimosho Local Government', 'Alimosho Local Government'),
    ('Amuwo-Odofin Local Government', 'Amuwo-Odofin Local Government'),
    ('Apapa Local Government', 'Apapa Local Government'),
    ('Badagry Local Government', 'Badagry Local Government'),
    ('Epe Local Government', 'Epe Local Government'),
    ('Eti-Osa Local Government', 'Eti-Osa Local Government'),
    ('Ibeju-Lekki Local Government', 'Ibeju-Lekki Local Government'),
    ('Ifako-Ijaiye Local Government', 'Ifako-Ijaiye Local Government'),
    ('Ikeja Local Government', 'Ikeja Local Government'),
    ('Ikorodu Local Government', 'Ikorodu Local Government'),
    ('Kosofe Local Government', 'Kosofe Local Government'),
    ('Lagos Island Local Government', 'Lagos Island Local Government'),
    ('Lagos Mainland Local Government', 'Lagos Mainland Local Government'),
    ('Mushin Local Government', 'Mushin Local Government'),
    ('Ojo Local Government', 'Ojo Local Government'),
    ('Oshodi-Isolo Local Government', 'Oshodi-Isolo Local Government'),
    ('Shomolu Local Government', 'Shomolu Local Government'),
    ('Surulere Local Government', 'Surulere Local Government'),
    ('other state in Nigeria','other state in Nigeria'),
    ('Outside Nigeria', 'Outside Nigeria'),)

    GRADE = (('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17'))

    email = models.EmailField(max_length=80,unique=True)
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=5,choices=GRADE,null=False)
    gender = models.CharField(max_length=6,choices=GENDER,null=False,default='MALE')
    qualification = models.CharField(max_length=60)
    date_birth = models.DateField(null=False,blank=False,default=datetime.now)
    state_origin = models.CharField(max_length=50,choices=LOCAL_GOVERNMENT)
    designation_appointement = models.CharField(max_length=150)
    date_first_appointment = models.DateField(null=False,blank=False,default=datetime.now)
    date_present_appointment = models.DateField(null=False,blank=False,default=datetime.now)
    employee_number = models.CharField(max_length=20)
    civil_service_number = models.CharField(max_length=20)
    mepb_file_number = models.CharField(max_length=20)
    present_post = models.CharField(max_length=500)
    mdas_posted = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    phone_num_nextofkin = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='images/',null=True,blank=True)
    biography = models.CharField(max_length=5000)
    status = models.CharField(max_length=20,choices=STATUS)
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class StaffNotification(models.Model):
    staff = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance)


@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.staff.save()






#testing 

# class Author(models.Model):
#     name = models.CharField(max_length=100)


#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title