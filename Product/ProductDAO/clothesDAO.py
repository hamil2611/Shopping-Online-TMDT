from email.mime import image
from multiprocessing import context
from turtle import pu
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Product.models import Book, Laptop,Mobilephone,Clothes,Category
def listcolothes(request):
    list_clothes = Clothes.objects.all()
    context = {"dsclothes":list_clothes}
    return render(request, "Clothes/viewclothes.html",context)
def saveclothes(request):
    category = Category.objects.get(product_type='Clothes')
    name = request.POST["ten"]
    brand = request.POST["hangsx"]
    size = request.POST["size"]
    color = request.POST["mau"]
    material = request.POST["chatlieu"]
    price = request.POST["gia"]
    images = request.FILES['anh']
    description = request.POST["mota"]
    quantity = request.POST["soluong"]
    c = Clothes.objects.create(name = name,brand=brand,size=size,color=color,material=material
    ,price=price,images=images,description=description,quantity=quantity,category_id=category
    )
    c.save()
    report = "Thêm sản phẩm thành công!"
    context = {"requestrp":report}
    return render(request, "Clothes/addclothes.html", context)
def deletelaptop(request, book_id):
    Book.objects.filter(book_id=book_id).delete()
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request,"homepage/laptop.html",context)
def pageaddclothes(request):
    return render(request,"Clothes/addclothes.html")