# context_processor.py
def Car_Total_Import(request):
    total = 120
    if request.user.is_authenticated:
        shopping_cart = request.session.get("ShoppingCart", {})
        for value in shopping_cart.values():
            total += float(value["Price"]) * value["Mount"]
    return {"Car_Total_Import": total}
