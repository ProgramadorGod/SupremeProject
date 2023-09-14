from django.shortcuts import render
from Blog.models import Post, Categories

# Create your views here.
def Blog(request):
    # Obtén todas las publicaciones y categorías
    categories = Categories.objects.all()
    posts = Post.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        posts = Post.objects.filter(Categories = category_id)
        return render(request, 'Blog/Blog.html', {"Posts": posts, "Categories": categories, "ID":int(category_id)})

    else:
        posts = Post.objects.all()
        category_id = 0
        return render(request, 'Blog/Blog.html', {"Posts": posts, "Categories": categories, "ID":int(category_id)})

    


