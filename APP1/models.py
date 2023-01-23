from django.db import models

# Create your models here.

class categorydb(models.Model):
    CategoryName =models.CharField(max_length=50, blank=True ,null=True)
    Brand =models.CharField(max_length=50, blank=True, null=True)
    Description =models.CharField(max_length=50, blank=True, null=True)
    Image =models.ImageField(upload_to="profile")

class westernwomendb(models.Model):
    DressName =models.CharField(max_length=50, blank=True ,null=True)
    Code =models.IntegerField( blank=True, null=True)
    Price =models.IntegerField( blank=True, null=True)
    Image =models.ImageField(upload_to="profile")


class westernmendb(models.Model):
    DressName =models.CharField(max_length=50, blank=True ,null=True)
    Code =models.IntegerField( blank=True, null=True)
    Price =models.IntegerField( blank=True, null=True)
    Image =models.ImageField(upload_to="profile")

class Accessoriesdb(models.Model):
    AccessoriesName =models.CharField(max_length=50, blank=True ,null=True)
    Code=models.IntegerField( blank=True, null=True)
    Price =models.IntegerField( blank=True, null=True)
    Image =models.ImageField(upload_to="profile")


class adminpagedb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    MobileNumber = models.IntegerField(null=True,blank=True)
    EmailID = models.EmailField(null=True,blank=True)
    Image = models.ImageField(upload_to="profile")
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    ConfirmPassword = models.CharField(max_length=50,null=True,blank=True)


class productdatabase(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")

class Contactdb(models.Model):
    EmailID=models.EmailField(max_length=50, null=True, blank=True)
    Message=models.CharField(max_length=100, null=True, blank=True)

class Blogdb(models.Model):
    Comment=models.CharField(max_length=50, null=True, blank=True)
    Name=models.CharField(max_length=50, null=True, blank=True)
    EmailID=models.EmailField(max_length=50, null=True, blank=True)
    Website=models.CharField(max_length=100, null=True, blank=True)