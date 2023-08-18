from django.shortcuts import render, HttpResponse


# Create your views here.

def Home(request):
    return render(request,'Home.html')


def Store(request):
    return render(request,'Store.html')

def Blog(request):
    return render(request,'Blog.html')
    
def Contact(request):
    return render(request,'Contact.html')
