from math import ceil

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request):
    # return HttpResponse("Hello")
    return render(request, "srtextile/home.html")


def about(request):
    return render(request, "srtextile/about.html")


def contact(request):
    return render(request, "srtextile/contact.html")


def products(request):
    # allProds=[]
    #
    # catprods = Product.objects.values('category')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])
    # # params = {'no_of_slides': nRows, 'range': range(0, nRows), 'product': products}
    # # allProds = [[products, range(1, nRows), nRows],
    # #             [products, range(1, nRows), nRows]]
    # params = {'allProds': allProds}
    # para={'name': 'usama'}
    # return HttpResponse(request, 'Usama')
    return render(request, "srtextile/test.html")


def productDesc(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "srtextile/productDesc.html", {'product':product})


def fabric(request):
    # return HttpResponse('Usama')
    return render(request, "srtextile/fabric.html")


def garment(request):
    # allProds = []
    #
    # catprods = Product.objects.values('category')
    # cats = {item['category'] for item in catprods}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'allProds': allProds}
    # # return render(request, "srtextile/test.html",params)
    return HttpResponse("Usama")
