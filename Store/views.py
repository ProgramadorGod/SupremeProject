from django.shortcuts import redirect, render
from Store.models import Product
from ShoppingCart.models import ProductRelation
from django.contrib.auth.decorators import login_required

# Create your views here.
def Store(request):
    user = request.user  # Obtiene el usuario actual

    if user.is_authenticated:
        Products = Product.objects.all()
        user_proucs = ProductRelation.objects.filter(
            user=request.user).values_list(
                "product", flat=True)

        user_proucs = Product.objects.filter(id__in=user_proucs)
        return render(request,'Store/Store.html',{
        "user_products": user_proucs,
        "Products":Products})
    else:
        return redirect('/authentication/')
        
