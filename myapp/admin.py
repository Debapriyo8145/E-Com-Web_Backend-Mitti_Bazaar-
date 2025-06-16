from django.contrib import admin
from .models import Category, Products, ProductImage
# Register your models here.

# Register Category normally
admin.site.register(Category)

# Inline admin for multiple images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

# Custom Product admin with inline images
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    inlines = [ProductImageInline]

# Register Products with custom admin
admin.site.register(Products, ProductAdmin)

admin.site.site_header = "Mitti Bazaar Administration"
admin.site.site_title = "Mitti Bazaar Admin Portal"
admin.site.index_title = "Welcome to Mitti Bazaar Admin"