from django.contrib import admin
from .models import Book,Laptop,Clothes,Mobilephone,Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Laptop)
admin.site.register(Clothes)
admin.site.register(Mobilephone)
admin.site.register(Category)