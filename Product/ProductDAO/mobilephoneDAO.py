from email.mime import image
from multiprocessing import context
from turtle import color, pu
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Product.models import Book, Laptop,Mobilephone,Category
def listmobile(request):
    list_mobile = Mobilephone.objects.all()
    context = {"dsmobile":list_mobile}
    return render(request, "Mobilephone/viewmobilephone.html",context)
def listmobile_customer(request):
    list_mobile = Mobilephone.objects.all()
    context = {"dsmobile":list_mobile}
    return render(request, "Mobilephone/see_all_mobile.html",context)    
def savemobile(request):
    category = Category.objects.get(product_type='Mobilephone')
    name = request.POST["ten"]
    brand = request.POST["hangsx"]
    size = request.POST["size"]
    color = request.POST["mau"]
    material = request.POST["chatlieu"]
    model = request.POST["kieumay"]
    price = request.POST["gia"]
    images = request.FILES['anh']
    description = request.POST["mota"]
    quantity = request.POST["soluong"]
    m = Mobilephone.objects.create(name = name,brand=brand,size=size,
    model=model,price=price,images=images,
    description=description,quantity=quantity,color=color,material=material,category_id=category
    )
    m.save()
    report = "Thêm sản phẩm thành công!"
    context = {"requestrp":report}
    return render(request, "Mobilephone/addmobilephone.html", context)
def deletelaptop(request, book_id):
    Book.objects.filter(book_id=book_id).delete()
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request,"homepage/laptop.html",context)
def pageaddmobilephone(request):
    return render(request,"Mobilephone/addmobilephone.html")