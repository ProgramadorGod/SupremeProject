from django.contrib import admin
from .models import Product, Category_Prod

# Register your models here.
class ProductFields(admin.ModelAdmin):
    readonly_fields=('Created','Updated')


admin.site.register(Product)
admin.site.register(Category_Prod,ProductFields)
