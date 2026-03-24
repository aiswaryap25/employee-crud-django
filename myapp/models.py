from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Employee(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,blank=False)
    name=models.CharField(max_length=20,blank=False,null=False,validators=[RegexValidator(regex=r'^[A-Za-z]+$',message="name should contain only letters without space")])
    phone=models.CharField(max_length=10,blank=False,unique=True,null=False,validators=[RegexValidator(regex=r'^[6-9]\d{9}$',message="enter valid 10 digit indian phone number")])
    email=models.EmailField(blank=False,null=False)
    place=models.CharField(max_length=20,blank=False,null=False,validators=[RegexValidator(regex=r'^[A-Za-z]+$',message="place should contain only letters without space")])
    GENDER_CHOICES=[('male','MALE'),('female','FEMALE')]
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES,blank=False,null=False)