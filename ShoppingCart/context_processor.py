
def Car_Total_Import(request):
    total = 0 
    if request.user.is_authenticated:
        for key,value in request.session["ShoppingCart"].items():
            total += float(value["Price"])*value["Mount"]
    return{"Car_Total_Import":total}
