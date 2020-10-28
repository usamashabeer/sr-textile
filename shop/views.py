from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    print(nSlides)
    params = {'no_of_slides': nSlides, 'range': range(1 , nSlides), 'product': products}
    return render(request, "shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    a=Product.objects.all()
    for x in a:
        product_name = x.product_name
        category = x.category
        price = x.price
        param = {
            'product_name':product_name,
            'category': category,
            'price': price
        }
    # print(a)
    # print(a.category)

    # a=Product.objects.last()
    # field_object = Product._meta.get_field('category')
    # field_value = getattr(a, field_object.attname)
    # print(field_value)
    return render(request, 'shop/ProductDetails.html',param)

def checkout(request):
    return HttpResponse("We are at checkout")
