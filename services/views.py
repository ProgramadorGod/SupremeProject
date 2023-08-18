from django.shortcuts import render
from services.models import Services as Sv


# Create your views here.
def Services(request):
    Services = Sv.objects.all()
    return render(request,'Services.html', {"Services":Services})