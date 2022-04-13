from email.mime import image
from multiprocessing import context
from turtle import pu
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book

# Create your views here.
def listbook(request):
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request, "Book/viewbook.html",context)

def cuslistbook(request):
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request, "Book/viewbook.html",context)

def addbook(request):
    title = request.POST["tensach"]
    summary = request.POST["namxuatban"]
    language = request.POST["ngonngu"]
    price = request.POST["gia"]
    author = request.POST["tacgia"]
    publisher = request.POST["nhaxuatban"]
    images = request.FILES['anh']
    b = Book.objects.create(title=title,
                            summary=summary,language=language,price=price,author=author,publisher=publisher,images=images

    )
    b.save()
    report = "Thêm sản phẩm thành công!"
    context = {"requestrp":report}
    return render(request,"Book/viewbook.html", context)

def xoa(request, book_id):
    Book.objects.filter(book_id=book_id).delete()
    list_book = Book.objects.all()
    context = {"dsbook":list_book}
    return render(request,"Book/viewbook.html",context)
def pageaddbook(request):
    return render(request,"Book/viewbook.html")