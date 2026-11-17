from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'category', 'price', 'sku', 'is_active'
    ]
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'description', 'sku']
    list_select_related = ['category']

