from multiprocessing import context
from re import T
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,decorators,logout
from Product.models import Book,Laptop,Mobilephone,Clothes
# Create your views here.
    
def handleLogout(request):
    logout(request)
    return render(request,"pages/home.html")

#register
def formregister(request):
    return render(request,"pages/register.html")

def adduser(request):
    username = request.POST.get("username", False)
    email = request.POST.get("email", False)
    password = request.POST.get("password", False)
    address =  request.POST.get("address", False)
    phonenumber = request.POST.get("phone", False)

    try:
        user = User.objects.get(username = username)
        msg = "Tài khoản đã tồn tại!"
        context={"msg":msg}
        return render(request,"pages/register.html",context)
    except User.DoesNotExist:
        u = User.objects.create_user(email=email,username=username,password=password,address=address,phonenumber=phonenumber)
        u.save()
        return render(request,"pages/login.html")

#login
def formlogin(request):
    return render(request,"pages/login.html")

def login(request):
    tk = request.POST.get('username')
    mk = request.POST.get('password')
    user = authenticate(username = tk, password = mk)

    if user is None:
        return render(request, "pages/login.html")
    else:
        request.session['username'] = tk
        list_book = Book.objects.all()[:4]
        list_laptop = Laptop.objects.all()[:4]
        list_mobile = Mobilephone.objects.all()[:4]
        list_clothes = Clothes.objects.all()[:4]
        context = {"dsbook":list_book,"dslaptop":list_laptop,"dsmobile":list_mobile,"dsclothes":list_clothes,"username":tk}
        return render(request, "Base/customer_viewlistproduct.html",context)
    

#showlist_product_customer
def customer_listproduct(request):
    username = request.session.get('username')
    list_book = Book.objects.all()[:4]
    list_laptop = Laptop.objects.all()[:4]
    list_mobile = Mobilephone.objects.all()[:4]
    list_clothes = Clothes.objects.all()[:4]
    context = {"dsbook":list_book,"dslaptop":list_laptop,"dsmobile":list_mobile,"dsclothes":list_clothes, "username": username}
    return render(request, "Base/customer_viewlistproduct.html",context)

#product_detail
def product_detail_book(request,book_id):
    username = request.session.get('username')
    book = Book.objects.get(pk=book_id)
    context = {"book":book, "username": username}
    return render(request,"Book/product_detail_book.html",context)

#login_phanquyen
# @decorators.login_required(login_url='/login/')
def view_cart(request):
    username = request.session.get('username')
    if not username:
        return render(request,"pages/login.html")
    else:
        context = {"username": username}
        return render(request,"Cart/cart.html",context)

# @decorators.login_required(login_url='/login/')
def add_to_cart(request, id):
    username = request.session.get('username')
    if not username:
        return render(request,"pages/login.html")
    else:
        context = {"username": username}
        return render(request,"Cart/cart.html",context)
