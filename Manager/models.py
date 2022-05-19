from secrets import choice
from tkinter.messagebox import NO
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length = 100,default=None)
    sex_choice =  ((0,"Nữ"), (1,"Nam"))
    sex = models.IntegerField(choices=sex_choice,default=0)
    address = models.CharField(max_length=100, default='')
    phonenumber = models.CharField(max_length=15, default='')
    def __str__(self):
        return self.get_short_name()
class Comment(models.Model):
    content = models.CharField(max_length=200,default=None)
    date = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)
    user = models.CharField(max_length=100,default=None)
class Shipment(models.Model):
    shipment_id = models.AutoField(primary_key=True,default=None)
    address = models.CharField(max_length=100,default=None)
    method_transport = models.CharField(max_length=100,default=None)
class Payment(models.Model):
    payment_id =models.AutoField(primary_key=True,default=None)
    payment_method = models.CharField(max_length=100, default="")
    totalprice = models.FloatField(default=None)
class Order(models.Model):
    order_id = models.AutoField(primary_key=True,default=None)
    payment_id = models.CharField(max_length=100,default=None)
    shipment_id = models.CharField(max_length=100,default=None)
    user = models.CharField(max_length=100,default=None)