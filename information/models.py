from django.db import models

# Create your models here.


class Information(models.Model):
    GENDER = (('MALE','M'),('FEMALE','F'))
    GRADE = (('GL1','GL1'),('GL2','GL2'),('GL3','GL3'),('GL4','GL4'),('GL5','GL5'),('GL6','GL6'),('GL7','GL7'),('GL8','GL8'),('GL9','GL9'),('GL10','GL10'),('GL12','GL12'),('GL13','GL13'),('GL14','GL14'),('GL15','GL15'),('GL16','GL16'),('GL17','GL17'))
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    grade_level = models.CharField(max_length=5,choices=GRADE,null=False)
    gender = models.CharField(max_length=6,choices=GENDER,null=False)

    
    
