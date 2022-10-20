from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Product

# Create your views here.

def index(request):
    

    li = ["Allen","Ansa","Allu"]

    context = {'names':li}

    return render(request, 'index.html',context=context)


def new_one(request):
    return HttpResponse("This is New one") 

def products(request):
    # p = Product.objects.filter(price__gt = 100000) 
    p = Product.objects.all() 

    context = {'products':p}

    return render(request, 'products.html',context=context)   

def product_details(request,id):

    p = Product.objects.get(id=id)

    context = {'p':p}

    return render(request, 'product_details.html',context=context)

def add_product(request):

    p = Product(name = "Samsung Monitor" ,price = 36000.00)

    p.description = "This is a Monitor"

    p.save()

    return HttpResponse(p)


