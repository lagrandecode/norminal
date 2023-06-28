from django.db import models

# Create your models here.


class Information(models.Model):
    GENDER = (('MALE','M'),('FEMALE','F'))
    GRADE = (('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17'))
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    # designation = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=5,choices=GRADE,null=False)
    gender = models.CharField(max_length=6,choices=GENDER,null=False)
    qualification = models.CharField(max_length=60)
    date_birth = models.DateField()
    # state_origin = models.CharField()
    designation_appointement = models.CharField()
    date_first_appointment = models.DateField()
    date_present_appointment = models.DateField()
    employee_number = models.CharField(max_length=20)
    civil_service_number = models.CharField(max_length=20)
    mepb_file_number = models.CharField(max_length=20)
    present_post = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    
    
