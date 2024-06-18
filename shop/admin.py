from django.contrib import admin
from .models import Category, Product, Cart, Testimonial
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'slug', 'image')
    prepopulated_fields = {'slug':('title', )}
    list_display_links = ('id', 'title', 'slug','image')
    search_fields = ('title', 'id')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'name', 'description_obj', 'price')
    list_display_links = ('id', 'name', 'description_obj', 'price')
    search_fields = ('name', 'id')
    ordering = ('id',)
    def description_obj(self, obj):
        return obj.description[:5]


@admin.register(Cart)
class CartAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'title', 'user')
    list_display_links = ('id', 'title', 'user')
    search_fields = ('title', 'id')
    ordering = ('id',)


@admin.register(Testimonial)
class TestiminialAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'description_obj', 'full_name')
    list_display_links = ('id', 'description_obj', 'full_name')
    search_fields = ('full_name', 'id')
    ordering = ('id',)

    def description_obj(self, obj):
        return obj.description[:5]
