from django.shortcuts import render
from Blog.models import Post

# Create your views here.
def Blog(request):
    Posts = Post.objects.all()
    return render(request,'Blog/Blog.html', {"Posts":Posts})