# context_processor.py
from ShoppingCart.models import ProductRelation


def Car_Total_Import(request):
    total = 0
    print("LOOL ", request.user.is_authenticated)

    if request.user.is_authenticated:
        shopping_cart = request.session.get("ShoppingCart", {})
        for value in shopping_cart.values():
            total += float(value["Price"]) * value["Mount"]
    return {"Car_Total_Import": total}


def TotalMount(request):
    user_products = ProductRelation.filter(user=request.user)
    product_quantities = {}

    for product in user_products:
        product_name = product.Name
        if product_name in product_quantities:
            product_quantities[product_name] +=1
        else:
            product_quantities[product_name] = 1

    context ={
        'user_products': user_products,
        'product_quantities': product_quantities,
    }

    return {'A':'A'}
    

