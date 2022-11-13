from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Product
# from django.db.models import Q
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,TemplateView,CreateView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    

    li = ["Allen","Ansa","Allu"]

    context = {'names':li}

    return render(request, 'myapp/index.html',context=context)


def new_one(request):
    return HttpResponse("This is New one") 

class ProductListView(ListView):
    model = Product
    template_name = 'myapp/products.html'
    context_object_name = 'products'   
    

@login_required
def products(request):
    # p = Product.objects.filter(price__gt = 100000) 
    p = Product.objects.all() 

    context = {'products':p}

    return render(request, 'myapp/products.html',context=context)   

def product_details(request,id):

    p = Product.objects.get(id=id)

    context = {'p':p}

    return render(request, 'myapp/product_details.html',context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_details.html'
    context_object_name = 'p'

@login_required
def add_product(request):
    if(request.method == 'POST'):
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES['upload']
        p = Product(name=name,price=price,description=description,image=image,seller=request.user)

        p.save()
        return redirect('myapp/products')
    
    return render(request, 'myapp/addproduct.html')


def update_product(request,id):
    p = Product.objects.get(id=id)

    context = {'p':p}

    if(request.method == 'POST'):
        p.name=request.POST.get('name')
        p.price=request.POST.get('price')
        p.description=request.POST.get('description')

        try:
            p.image=request.FILES['upload']
        except:
         pass 
        # p = Product(name=name,price=price,description=description,image=image)

        p.save()
        return redirect('myapp/products')
    
    return render(request, 'myapp/update_product.html',context=context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name','price','description','image','seller']
    template_name = 'myapp/update_product.html'
    context_object_name = 'p'
    success_url = reverse_lazy('myapp:products')
    

def delete_product(request,id):
    p = Product.objects.get(id=id)

    context = {'p':p}

    if(request.method == 'POST'):
        p.delete()
       
        return redirect('myapp/products')
    
    return render(request, 'myapp/delete_product.html',context=context)

class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'p'
    success_url = reverse_lazy('myapp:products')

