from secrets import choice
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    sex_choice =  ((0,"Nữ"), (1,"Nam"))
    sex = models.IntegerField(choices=sex_choice,default=0)
    address = models.CharField(max_length=100, default='')
    phonenumber = models.CharField(max_length=15, default='')
    