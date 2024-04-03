from django.contrib import admin
from .models import Category, Product, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
	list_display =['id', 'name']
	# prepopulated_fields = {'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
