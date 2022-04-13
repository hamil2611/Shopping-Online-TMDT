from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views,name="index"),
    path('viewbook/',views.listbook,name="viewbook"),
]