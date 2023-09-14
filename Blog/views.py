from django.shortcuts import render
from Blog.models import Post, Categories

# Create your views here.
def Blog(request):
    # Obtén todas las publicaciones y categorías
    posts = Post.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(Categories = category_id)
    categories = Categories.objects.all()
    
    return render(request, 'Blog/Blog.html', {"Posts": posts, "Categories": categories, "ID":category_id})


