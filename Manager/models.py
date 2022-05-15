from secrets import choice
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sex_choice =  ((0,"Nữ"), (1,"Nam"))
    sex = models.IntegerField(choices=sex_choice,default=0)
    address = models.CharField(max_length=100, default='')
    phonenumber = models.CharField(max_length=15, default='')
class Comment(models.Model):
    content = models.CharField(max_length=200,default=None)
    date = models.DateTimeField(auto_now_add=True)
    product_id = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)
    user = models.CharField(max_length=100,default=None)
