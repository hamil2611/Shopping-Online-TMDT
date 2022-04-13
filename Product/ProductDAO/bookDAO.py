from email.mime import image
from multiprocessing import context
from turtle import pu
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Product.models import Book,Category

# Create your views here.
def listbook(request):
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request, "Book/viewbook.html",context)

def listbook_customer(request):
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request, "Book/customer_viewbook.html",context)

def customer_listbook(request):
    list_book = Book.objects.all()[:4]
    context = {"dsbook":list_book}
    return render(request, "Book/customer_viewbook.html",context)

def savebook(request):
    category = Category.objects.get(product_type='Sách')
    title = request.POST["tensach"]
    summary = request.POST["namxuatban"]
    language = request.POST["ngonngu"]
    price = request.POST["gia"]
    author = request.POST["tacgia"]
    publisher = request.POST["nhaxuatban"]
    images = request.FILES['anh']
    description = request.POST["mota"]
    quantity = request.POST["soluong"]
    b = Book.objects.create(title=title,summary=summary,language=language,price=price,author=author,
                            publisher=publisher,images=images,description=description,quantity=quantity,category_id=category)
    b.save()
    report = "Thêm sản phẩm thành công!"
    context = {"requestrp":report}
    return render(request,"Book/addbook.html", context)

def deletebook(request, book_id):
    Book.objects.filter(book_id=book_id).delete()
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request,"Book/viewbook.html",context)

def pageaddbook(request):
    return render(request,"Book/addbook.html")