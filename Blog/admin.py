from django.contrib import admin
from .models import Categories,Post

class CategoriesAdmin(admin.ModelAdmin):
    readonly_fields = ('Created', 'Updated')


class PostsAdmin(admin.ModelAdmin):
    readonly_fields = ('Created', 'Updated')


admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Post,PostsAdmin)