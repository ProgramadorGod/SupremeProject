from django.contrib import admin

from ShoppingCart.models import ProductRelation


@admin.register(ProductRelation)
class ProductRelationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "product"
    )
