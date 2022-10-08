from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    

    li = ["Allen","Ansa","Allu"]

    context = {'names':li}

    return render(request, 'index.html',context=context)


def new_one(request):
    return HttpResponse("This is New one")  
