from django.shortcuts import render
from Blog.models import Post, Categories

# Create your views here.
def Blog(request):
    # Obtén todas las publicaciones y categorías
    categories = Categories.objects.all()

    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(Categories = category_id)
    else:
        posts = Post.objects.all()

    
    return render(request, 'Blog/Blog.html', {"Posts": posts, "Categories": categories, "ID":category_id})


