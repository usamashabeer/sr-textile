from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("https://sr-textile.herokuapp.com/srtextile/AboutUs/", views.about, name="AboutUs"),
    path("ContactUs/", views.contact, name="ContactUs"),
    path("Product/", views.products, name="Products"),
    path("FabricGuide/", views.fabric, name="FabricGuide"),
    path("ProductDesc/<int:myid>", views.productDesc, name="ProductDesc"),
]