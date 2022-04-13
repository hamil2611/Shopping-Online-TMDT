from multiprocessing import context
from re import T
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth import authenticate,decorators,logout
from Product.models import Book,Laptop,Mobilephone,Clothes

# Create your views here.
    
def logout(request):
    logout(request)
    return HttpResponse("!@#1231233")

#register
def formregister(request):
    return render(request,"pages/register.html")
def adduser(request):
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    username = request.POST["username"]
    password = request.POST["password"]
    address =  request.POST["address"]
    phonenumber="2432423423"
    check = User.objects.get(username=username)
    if check is None:
        u = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password,
        address=address,phonenumber=phonenumber)
        u.save()
        return render(request,"Base/base.html")
    else:
        msg = "Tài khoản đã tồn tại!"
        context={"msg":msg}
        return render(request,"pages/register.html",context)
#login
def formlogin(request):
    return render(request,"pages/login.html")

def login(request):
    tk = request.POST.get('username')
    mk = request.POST.get('password')
    check = authenticate(username = tk, password = mk)
    if check is None:
        return render(request,"Base/base.html")
    else: 
        if  tk =="admin" and mk =="admin":
            return render(request,"Base/base.html")
        else:
            u = User.objects.get(username=tk)
            list_book = Book.objects.all()[:4]
            list_laptop = Laptop.objects.all()[:4]
            list_mobile = Mobilephone.objects.all()[:4]
            list_clothes = Clothes.objects.all()[:4]
            context = {"dsbook":list_book,"dslaptop":list_laptop,"dsmobile":list_mobile,"dsclothes":list_clothes,"user":u}
            return render(request, "Base/customer_viewlistproduct.html",context)
    

#showlist_product_customer
def customer_listproduct(request):
    list_book = Book.objects.all()[:4]
    list_laptop = Laptop.objects.all()[:4]
    list_mobile = Mobilephone.objects.all()[:4]
    list_clothes = Clothes.objects.all()[:4]
    context = {"dsbook":list_book,"dslaptop":list_laptop,"dsmobile":list_mobile,"dsclothes":list_clothes}
    return render(request, "Base/customer_viewlistproduct.html",context)

#product_detail
def product_detail_book(request,book_id):
    book = Book.objects.get(pk=book_id)
    context = {"book":book}
    return render(request,"Book/product_detail_book.html",context)

#login_phanquyen
@decorators.login_required(login_url='/login/')
def view_cart(request):
    return render(request,"Cart/cart.html")

@decorators.login_required(login_url='/login/')
def add_to_cart(request, book_id):
    return render(request,"Base/customer_viewlistproduct.html")
