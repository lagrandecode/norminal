from django.db import models

# Create your models here.


class Information(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    other_name = models.CharField(max_length=200)
    
    
