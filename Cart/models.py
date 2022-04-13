from itertools import product
from unicodedata import category
from django.db import models
from Product.models import Book,Laptop,Mobilephone,Clothes
from Manager.models import User
# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True,default=None)
    quantity = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    category_id = models.IntegerField(default=0)
    customer = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
