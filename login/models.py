from django.db import models

Status_options=(('user','User'),('doctor','Doctor'),('hospital','Hospital'))
# Create your models here.
class User(models.Model):
    User_id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=150,verbose_name="Username",blank=True, null=False)
    User_email=models.EmailField(max_length=200, verbose_name="User Email", blank=True, null=False,unique=True)
    User_contact=models.PositiveBigIntegerField(max_length=20,verbose_name="Contact number",blank=True,null=False)
    User_profile=models.ImageField(verbose_name="User Profile")
    User_address=models.CharField(max_length=200,verbose_name="Address",blank=True,null=False)
    User_password=models.CharField(max_length=100,verbose_name="Password",blank=True,null=False)
    User_status=models.CharField(max_length=1,choices=Status_options)

class Doctor(models.Model):
    Doctor_id=models.AutoField(primary_key=True)
    Doctor_username=models.CharField(max_length=150,verbose_name="Doctor name",blank=True, null=False)
    Doctor_email=models.EmailField(max_length=200, verbose_name="Doctor Email", blank=True, null=False)
    Doctor_profile=models.ImageField(verbose_name="Doctor Profile")
    Doctor_address=models.CharField(max_length=200,verbose_name="Address",blank=True,null=False)
    Doctor_password=models.CharField(max_length=250,verbose_name="Password",blank=True,null=False)
    Doctor_status=models.CharField(max_length=1,choices=Status_options)

class Hospital(models.Model):
    Hospital_id=models.AutoField(primary_key=True)
    Hospital_username=models.CharField(max_length=150,verbose_name="Hospital name",blank=True, null=False)
    Hospital_email=models.EmailField(max_length=200, verbose_name="Hospital Email", blank=True, null=False)
    Hospital_contact=models.PositiveBigIntegerField(max_length=20,verbose_name="Contact number",blank=True,null=False)
    Hospital_profile=models.ImageField(verbose_name="Hospital Profile")
    Hospital_address=models.CharField(max_length=200,verbose_name="Address",blank=True,null=False)
    Hospital_password=models.CharField(max_length=250,verbose_name="Password",blank=True,null=False)
    Hospital_status=models.CharField(max_length=1,choices=Status_options)
