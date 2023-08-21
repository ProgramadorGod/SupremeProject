from django.shortcuts import render, HttpResponse


# Create your views here.

def Home(request):
    return render(request,'SupremeApp/Home.html')

def Store(request):
    return render(request,'SupremeApp/Store.html')

def Contact(request):
    return render(request,'SupremeApp/Contact.html')
