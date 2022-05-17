from django.contrib import admin
from django.urls import path,include
from . import views
from Product.ProductDAO import bookDAO, laptopDAO,mobilephoneDAO,clothesDAO
urlpatterns = [
    #index

    path('',views.customer_listproduct,name="index"),
    # path('',bookDAO.customer_listlaptop,name="index"),
    # path('',bookDAO.customer_listclothes,name="index"),
    # path('',bookDAO.customer_listbook,name="index"),

    #Login
    path('login/',views.formlogin,name="login"),
    path('homepage/',views.login,name="checklogin"),

    #logout
    path('logout/',views.handleLogout,name="logout"),

    #register
    path('register/',views.formregister,name="register"),
    path('registeruser/',views.adduser,name="registeruser"),

    #Book
    path('viewbook/',bookDAO.listbook,name="viewbook"),#view manager
    path('viewbook/<int:book_id>', bookDAO.deletebook, name="delete"),
    path('pageaddbook/', bookDAO.pageaddbook, name="pageaddbook"),
    path('savebook/', bookDAO.savebook, name="savebook"),
    path('see_all_book/', bookDAO.listbook_customer, name="see_all_book"),
    
    #Laptop
    path('viewlaptop/',laptopDAO.listlaptop,name="viewlaptop"),
    path('viewbook/<int:book_id>', bookDAO.deletebook, name="delete"),
    path('pageaddlaptop/',laptopDAO.pageaddlaptop, name="pageaddlaptop"),
    path('savelaptop/', laptopDAO.savelaptop, name="savelaptop"),

    #Mobilephone
    path('viewmobilephone/',mobilephoneDAO.listmobile,name="viewmobilephone"),
    path('pageaddmobilephone/',mobilephoneDAO.pageaddmobilephone,name="pageaddmobilephone"),
    path('savemobilephone/', mobilephoneDAO.savemobile, name="savemobilephone"),

    #Clothes 
    path('viewclothes/',clothesDAO.listcolothes,name="viewclothes"),
    path('pageaddclothes/',clothesDAO.pageaddclothes,name="pageaddclothes"),
    path('saveclothes/', clothesDAO.saveclothes, name="saveclothes"),
    #Product_detail
    
    path('product_detail/id=<int:id>',views.product_detail_book,name="product_detail_book"),

    #Add_To_Cart
    path('viewcart/id=<int:id>/quantity=<int:quantity>/category=<int:category>',views.add_to_cart,name="add_to_cart"),
    path('viewcart/',views.view_cart,name="viewcart"),

    #Addcoment
    path('product_detail/id=<int:book_id>',views.addcomment,name="addcomment"),
]
