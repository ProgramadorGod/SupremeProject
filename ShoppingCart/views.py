from django.shortcuts import render
from Car import *
from Store.models import Product
from django.shortcuts import redirect


# Create your views here.

def AddProduct(request, Product_ID):
    Cart = Car(request)
    Product = Product.objects.get(id = Product_ID)
    Cart.AddProducts(Product=Product)

    return redirect("Store")


def Substract(request, Product_ID):
    Cart = Car(request)
    Product = Product.objects.get(id = Product_ID)
    Cart.SubtractPds(Product=Product)
    return redirect("Store")

def DeleteProduct(request, Product_ID):
    Cart = Car(request)
    Product = Product.objects.get(id = Product_ID)
    Cart.Delete(Product=Product)

    return redirect("Store")

def Clean(request, Product_ID):
    Cart = Car(request)
    Cart.EmptyCart()
    