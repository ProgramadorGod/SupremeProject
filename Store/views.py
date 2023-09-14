from django.shortcuts import render
from Store.models import Product

# Create your views here.
def Store(request):
    Products = Product.objects.all()
    return render(request,'Store/Store.html',{"Products":Products})