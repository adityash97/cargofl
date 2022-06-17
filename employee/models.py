from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    MARITIAL_STATUS = [
        ('M','Married'),
        ('N','Not Married')
    ]

    BLOOD_GROUP = [
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('O+','O+'),
        ('O-','O-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
    ]
    employee_first_name = models.CharField(max_length = 50,null=False, blank=False)
    employee_middle_name = models.CharField(max_length = 50,blank=True)
    employee_last_name = models.CharField(max_length = 50,null=False, blank=False)
    gender = models.CharField(max_length = 1,choices=GENDER,null=False, blank=False)
    mobile_number = models.IntegerField(null=False, blank=False)
    date_of_birth = models.DateField( null=True,blank=True)
    alternate_mobile_number = models.IntegerField( null=True,blank=True)
    email_id = models.EmailField(max_length = 50,null=False, blank=False)
    maritial_staus = models.CharField(max_length = 1,choices=MARITIAL_STATUS,null=False, blank=False)
    blood_group = models.CharField(max_length = 3,choices=BLOOD_GROUP,null=False, blank=False)

    def __str__(self):
        return self.employee_first_name+' '+self.employee_last_name 
