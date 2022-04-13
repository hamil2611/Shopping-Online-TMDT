from email.mime import image
from multiprocessing import context
from turtle import pu
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Product.models import Book, Laptop,Category
def listlaptop(request):
    list_laptop = Laptop.objects.all()
    context = {"dslaptop":list_laptop}
    return render(request, "Laptop/viewlaptop.html",context)
def savelaptop(request):
    category = Category.objects.get(product_type='Laptop')
    name = request.POST["tenlaptop"]
    brand = request.POST["hangsx"]
    screensize = request.POST["size"]
    model = request.POST["kieumay"]
    price = request.POST["gia"]
    images = request.FILES['anh']
    description = request.POST["mota"]
    quantity = request.POST["soluong"]
    l = Laptop.objects.create(name = name,brand=brand,screensize=screensize,
    model=model,price=price,images=images,description=description,quantity=quantity,category_id=category
    )
    l.save()
    report = "Thêm sản phẩm thành công!"
    context = {"requestrp":report}
    return render(request, "Laptop/addlaptop.html", context)
def deletelaptop(request, book_id):
    Book.objects.filter(book_id=book_id).delete()
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request,"homepage/laptop.html",context)
def pageaddlaptop(request):
    return render(request,"Laptop/addlaptop.html")