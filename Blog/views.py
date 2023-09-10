from django.shortcuts import render
from Blog.models import Post, Categories

# Create your views here.
def Blog(request):
    Posts = Post.objects.all()
    
    # Crear una lista para almacenar las categorías únicas
    unique_categories = []
    
    for post in Posts:
        categories = post.Categories.all()
        for category in categories:
            # Verificar si la categoría ya está en la lista
            if category not in unique_categories:
                unique_categories.append(category)
    
    return render(request, 'Blog/Blog.html', {"Posts": Posts, "Categories": unique_categories})


#def Category(request):
    Categoriez = Categories.objects.all()
    return render(request,'Blog/Blog.html', {"Categoriez":Categoriez})

