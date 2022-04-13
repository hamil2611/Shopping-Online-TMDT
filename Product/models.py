from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import FALSE
from pyexpat import model
from statistics import mode
from traceback import StackSummary
from turtle import color, title
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True,default=None)
    product_type = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.product_type
        
class Book(models.Model):
    book_id = models.AutoField(primary_key=True,default=None)
    title = models.CharField(max_length=100,default='')
    summary = models.CharField(max_length=100,default='')
    language = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    author = models.CharField(max_length=100,default='')
    publisher = models.CharField(max_length=100,default='')
    images = models.ImageField(upload_to='image', null=FALSE, default=None)
    description = models.CharField(default='',max_length=1000)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category,null=None,on_delete=models.CASCADE)

class Laptop(models.Model):
    laptop_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    brand = models.CharField(max_length=100,default='')
    screensize = models.CharField(max_length=100,default='')
    model = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    images= models.ImageField(upload_to='image', null = FALSE, default=None)
    description = models.CharField(default='',max_length=1000)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)

class Clothes(models.Model):
    clothes_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    brand = models.CharField(max_length=100,default='')
    size = models.CharField(max_length=100,default='')
    color = models.CharField(max_length=100,default='')
    material = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    images= models.ImageField(upload_to='image', null = FALSE, default=None)
    description = models.CharField(default='',max_length=1000)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)

class Mobilephone(models.Model):
    mobile_id = models.AutoField(primary_key=True,default=None)
    name = models.CharField(max_length=100,default='')
    brand = models.CharField(max_length=100,default='')
    size = models.CharField(max_length=100,default='')
    color = models.CharField(max_length=100,default='')
    material = models.CharField(max_length=100,default='')
    price = models.FloatField(default=0)
    model = models.CharField(max_length=100,default='')
    images= models.ImageField(upload_to='image', null = FALSE, default=None)
    description = models.CharField(default='',max_length=1000)
    quantity = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)
