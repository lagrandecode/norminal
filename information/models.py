from django.db import models

# Create your models here.


class Information(models.Model):
    STATUS = [('ACTIVE','ACTIVE'),('RETIRED','RETIRED'),('RESIGNED','RESIGNED'),('OTHERS','OTHERS')]
    GENDER = (('MALE','M'),('FEMALE','F'))
    LOCAL_GOVERNEMNT = (('Agege Local Government','Agege Local Government'),('Ajeromi-Ifelodun Local Government','Ajeromi-Ifelodun Local Government'),('Alimosho Local Government','Alimosho Local Government'),('Amuwo-Odofin Local Government','Amuwo-Odofin Local Government'),
    ('Apapa Local Government','Apapa Local Government'),('Badagry Local Government','Badagry Local Government'),('Epe Local Government','Epe Local Government'),('Eti-Osa Local Government','Eti-Osa Local Government'),('Ibeju-Lekki Local Government','Ibeju-Lekki Local Government'),('Ifako-Ijaiye Local Government','Ifako-Ijaiye Local Government'),('Ikeja Local Government','Ikeja Local Government'),('Ikorodu Local Government','Ikorodu Local Government'),('Kosofe Local Government','Kosofe Local Government','Lagos Island Local Government','Lagos Island Local Government'),('Lagos Mainland Local Government','Lagos Mainland Local Government'),('Mushin Local Government','Mushin Local Government'),('Ojo Local Government','Ojo Local Government'),('Oshodi-Isolo Local Government','Oshodi-Isolo Local Government'),('Shomolu Local Government','Shomolu Local Government'),('Surulere Local Government','Surulere Local Government'),('outside Nigeria','outside Nigeria'))
    GRADE = (('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17'))
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    # designation = models.CharField(max_length=200) added by admin 
    # department = models.CharField(max_length=200) added by admin 

    grade_level = models.CharField(max_length=5,choices=GRADE,null=False)
    gender = models.CharField(max_length=6,choices=GENDER,null=False)
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
    phone_number = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='images/',null=True,blank=True)
    status = models.CharField(max_length=20,choices=STATUS)

    
    
