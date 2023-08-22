from django.shortcuts import render
from Store.models import Product,Category_Prod

# Create your views here.
def Store(request):
    Products = Product.objects.all()
    return render(request,'Store/Store.html',{"Products":Products})