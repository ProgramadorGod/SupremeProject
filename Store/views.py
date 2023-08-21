from django.shortcuts import render

# Create your views here.
def Store(request):
    return render(request,'SupremeApp/Store.html')