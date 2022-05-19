from audioop import add
from multiprocessing import context
from re import S
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect, HttpResponseRedirect
from Cart.models import Cart
from .models import Order, Payment, Shipment, User, Comment
from django.contrib.auth import authenticate, decorators, logout
from Product.models import Book, Laptop, Mobilephone, Clothes
from django.shortcuts import get_object_or_404
# Create your views here.

def handleLogout(request):
    logout(request)
    context = getListItem()
    return render(request, "Base/customer_viewlistproduct.html", context)

# register
def formregister(request):
    return render(request, "pages/register.html")

def adduser(request):
    username = request.POST.get("username", False)
    firstname = request.POST.get("firstname", False)
    email = request.POST.get("email", False)
    password = request.POST.get("password", False)
    address = request.POST.get("address", False)
    phonenumber = request.POST.get("phone", False)
    try:
        user = User.objects.get(username=username)
        msg = "Tài khoản đã tồn tại!"
        context = {"msg": msg}
        return render(request, "pages/register.html", context)
    except User.DoesNotExist:
        u = User.objects.create_user(first_name=firstname,
            email=email, username=username, password=password, address=address, phonenumber=phonenumber)
        u.save()
        return render(request, "pages/login.html")

# login
def formlogin(request):
    return render(request, "pages/login.html")

def login(request):
    tk = request.POST.get('username')
    mk = request.POST.get('password')
    user = authenticate(username=tk, password=mk)
    if user is None:
        return render(request, "pages/login.html")
    elif user.is_superuser:
        return render(request, "Base/base.html")
    else:
        request.session['username'] = tk
        first = getFirstname(request)
        list_book = Book.objects.all()[:4]
        list_laptop = Laptop.objects.all()[:4]
        list_mobile = Mobilephone.objects.all()[:4]
        list_clothes = Clothes.objects.all()[:4]
        context = {"dsbook": list_book, "dslaptop": list_laptop,
                   "dsmobile": list_mobile, "dsclothes": list_clothes, "username": first}
        return render(request, "Base/customer_viewlistproduct.html", context)

# showlist_product_customer
def customer_listproduct(request):
    
    context = getListItem()
    username = request.session.get('username')
    if username:
        context['username'] = getFirstname(request)
    return render(request, "Base/customer_viewlistproduct.html", context)

# product_detail
def product_detail_book(request, id):
    username = request.session.get('username')
    if username:
        username = getFirstname(request)
    book = Book.objects.get(pk=id)
    cate_id = book.category_id.category_id
    name = request.session.get('username')
    comment = Comment.objects.filter(product_id=id,category_id=cate_id).order_by('-id')[:4]
    context = {"book": book, "username": username,"comment":comment,"name":name}
    if request.method == 'POST':
        content = request.POST["content"]
        c = Comment.objects.create(content=content,product_id=id,user=name,category_id = cate_id)
        c.save()
        return HttpResponseRedirect(request.path)
    return render(request, "Book/product_detail_book.html", context)

def product_detail_laptop(request, id):
    username = request.session.get('username')
    if username:
        username = getFirstname(request)
    laptop = Laptop.objects.get(pk=id)
    cate_id = laptop.category_id.category_id
    name = request.session.get('username')
    comment = Comment.objects.filter(product_id=id,category_id=cate_id).order_by('-id')[:4]
    context = {"laptop": laptop, "username": username,"comment":comment,"name":name}
    if request.method == 'POST':
        content = request.POST["content"]
        c = Comment.objects.create(content=content,product_id=id,user=name,category_id = cate_id)
        c.save()
        return HttpResponseRedirect(request.path)
    return render(request, "Laptop/product_detail_laptop.html", context)

def product_detail_mobile(request, id):
    username = request.session.get('username')
    if username:
        username = getFirstname(request)
    mobile = Mobilephone.objects.get(pk=id)
    cate_id = mobile.category_id.category_id
    name = request.session.get('username')
    comment = Comment.objects.filter(product_id=id,category_id=cate_id).order_by('-id')[:4]
    context = {"mobile": mobile, "username": username,"comment":comment,"name":name}
    if request.method == 'POST':
        content = request.POST["content"]
        c = Comment.objects.create(content=content,product_id=id,user=name,category_id = cate_id)
        c.save()
        return HttpResponseRedirect(request.path)
    return render(request, "Mobilephone/product_detail_mobile.html", context)

def product_detail_clothes(request, id):
    username = request.session.get('username')
    if username:
        username = getFirstname(request)
    clothes = Clothes.objects.get(pk=id)
    cate_id = clothes.category_id.category_id
    name = request.session.get('username')
    comment = Comment.objects.filter(product_id=id,category_id=cate_id).order_by('-id')[:4]
    context = {"clothes": clothes, "username": username,"comment":comment,"name":name}
    if request.method == 'POST':
        content = request.POST["content"]
        c = Comment.objects.create(content=content,product_id=id,user=name,category_id = cate_id)
        c.save()
        return HttpResponseRedirect(request.path)
    return render(request, "Clothes/product_detail_clothes.html", context)    

# @decorators.login_required(login_url='/login/')


def view_cart(request):
    username = request.session.get('username')
    
    if not username:
        return render(request, "pages/login.html")
    else:
        context = getCart(username,request)
        return render(request, "Cart/cart.html", context)

# @decorators.login_required(login_url='/login/')
def add_to_cart(request, id, quantity, category):
    username = request.session.get('username')
    context = getCart(username,request)
    if not username:
        return render(request, "pages/login.html")
    else:
        customer = User.objects.get(username=username)
        if Cart.objects.filter(customer=customer, product_id=id, category_id=category).exists():
            oldCartItem = Cart.objects.get(customer=customer,
                                           product_id=id, category_id=category)
            newQuantity = oldCartItem.quantity + quantity
            Cart.objects.filter(customer=customer, product_id=id,
                                category_id=category).update(quantity=newQuantity)
            return HttpResponseRedirect("/home/")
        else:
            cartItem = Cart.objects.create(
                quantity=quantity, product_id=id, category_id=category, customer=customer)
            cartItem.save()
            return HttpResponseRedirect("/home/")
        
    #return render(request, "Cart/cart.html", context)
def checkout(request):
    username = request.session.get('username')
    context = getCart(username,request)
    if request.method == 'POST':
        address = request.POST["diachi"]
        method_transport = request.POST["hinhthuc"]
        ship = Shipment.objects.create(address=address,method_transport=method_transport)
        ship.save()
        ship_id = Shipment.objects.all().last()
        shipment_id=ship_id.shipment_id
        customer = User.objects.get(username=username)
        list = Cart.objects.all().filter(customer=customer)
        listBook = []
        listLaptop = []
        listClothes = []
        listMobilePhone = []
        for item in list:
            if getCartItemBook(item): listBook.append(getCartItemBook(item))
            if getCartItemLaptop(item): listLaptop.append(getCartItemLaptop(item))
            if getCartItemClothes(item): listClothes.append(getCartItemClothes(item))
            if getCartItemMobilePhone(item): listMobilePhone.append(getCartItemMobilePhone(item))
        totalPrice = getTotalPrice(listBook)
        pay = Payment.objects.create(totalprice =totalPrice)
        pay_id = Payment.objects.all().last()
        o = Order.objects.create(shipment_id=shipment_id,payment_id=pay_id.payment_id, user = username)
        o.save()
        Cart.objects.all().delete()
        return HttpResponseRedirect("/home/")
    return render(request,"pages/checkout.html",context)
# Common
def getListItem():
    list_book = Book.objects.all()[:4]
    list_laptop = Laptop.objects.all()[:4]
    list_mobile = Mobilephone.objects.all()[:4]
    list_clothes = Clothes.objects.all()[:4]
    context = {"dsbook": list_book, "dslaptop": list_laptop,
               "dsmobile": list_mobile, "dsclothes": list_clothes}
    return context


def getCart(username,request):
    customer = User.objects.get(username=username)
    list = Cart.objects.all().filter(customer=customer)

    listBook = []
    listLaptop = []
    listClothes = []
    listMobilePhone = []
    for item in list:
        if getCartItemBook(item): listBook.append(getCartItemBook(item))
        if getCartItemLaptop(item): listLaptop.append(getCartItemLaptop(item))
        if getCartItemClothes(item): listClothes.append(getCartItemClothes(item))
        if getCartItemMobilePhone(item):
            listMobilePhone.append(getCartItemMobilePhone(item))
    totalPrice = float(getTotalPrice(listBook)) 
    context = {'listBook': listBook,
               'listLaptop': listLaptop, 'listClothes': listClothes, 'listMobilePhone': listMobilePhone, 'totalPrice': totalPrice}
    context['username'] = getFirstname(request)
    return context


def getCartItemBook(item):
    try:
        book = Book.objects.get(book_id=item.product_id, category_id=item.category_id)
        bookItem = {'book': book, 'totalPrice': book.price *
                    item.quantity, 'quantity': item.quantity}
        return bookItem
    except Book.DoesNotExist:
        return 

def getCartItemLaptop(item):
    try:
        laptop = Laptop.objects.get(
            laptop_id=item.product_id, category_id=item.category_id)
        laptopItem = {'laptop': laptop, 'totalPrice': laptop.price *
                      item.quantity, 'quantity': item.quantity}
        return laptopItem
    except Laptop.DoesNotExist:
        return 


def getCartItemClothes(item):
    try:
        clothes = Clothes.objects.get(
            clothes_id=item.product_id, category_id=item.category_id)
        clothesItem = {'clothes': clothes, 'totalPrice': clothes.price *
                       item.quantity, 'quantity': item.quantity}
        return clothesItem
    except Clothes.DoesNotExist:
        return


def getCartItemMobilePhone(item):
    try:
        phone = Mobilephone.objects.get(
            mobile_id=item.product_id, category_id=item.category_id)
        phoneItem = {'phone': phone, 'totalPrice': phone.price *
                    item.quantity, 'quantity': item.quantity}
        return phoneItem
    except Mobilephone.DoesNotExist:
        return 


def getTotalPrice(list):
    total = 0 
    for item in list:
        total += item['totalPrice']
    return total

def getFirstname(request):
    username = request.session.get('username')
    firstname = User.objects.get(username=username)
    
    return firstname

@decorators.login_required(login_url='/login/')
def addcomment(request,book_id):
    
    content = request.POST["content"]
    name = request.session.get('username')
    print(content)
    print(book_id)
    print(name)
    c = Comment.objects.create(content=content,product_id=book_id,user=name)
    c.save()
    return render(request, "pages/login.html")

def view_checkout(request):
    return render(request, "pages/checkout.html")


def view_order(request):
    return render(request, "pages/view-order.html")
