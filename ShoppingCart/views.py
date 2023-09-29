# views.py
from django.shortcuts import render, redirect
from Store.models import Product
from ShoppingCart.Car import Car  # Importa la clase Car desde el módulo Car

def AddProduct(request, Product_Id):
    Cart = Car(request)
    product = Product.objects.get(id=Product_Id)
    print(request.user)
    print(product)
    Cart.AddProduct(product, request.user)

    return redirect("Store")

def Subtract(request, Product_Id):
    Cart = Car(request)
    product = Product.objects.get(id=Product_Id)
    Cart.SubtractPds(product, request.user)
    return redirect("Store")

def DeleteProduct(request, Product_Id):
    Cart = Car(request)
    product = Product.objects.get(id=Product_Id)
    Cart.Delete(product, request.user)

    return redirect("Store")

def Clean(request):
    Cart = Car(request)
    Cart.EmptyCart(request.user)
    return redirect("Store")

# Otras vistas que puedas tener...

    