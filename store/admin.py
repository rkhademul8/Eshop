from django.contrib import admin
from .models import product, Category
# Register your models here.

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','category','description','image']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']


admin.site.register(product, Adminproduct)
admin.site.register(Category,AdminCategory )