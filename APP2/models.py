from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    username=models.CharField(max_length=50, null=True, blank=True)
    email=models.EmailField(max_length=50, null=True, blank=True)
    password=models.CharField(max_length=50, null=True, blank=True)
    confirmpassword=models.CharField(max_length=50, null=True, blank=True)


class cartdb(models.Model):
    ProductName=models.CharField(max_length=50, null=True, blank=True)
    Description=models.CharField(max_length=50, null=True, blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    Image= models.ImageField(upload_to="profile", null=True)