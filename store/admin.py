from django.contrib import admin
from .models import Customer, product, Category
# Register your models here.


class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'phone', 'email', 'password']

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','category','description','image']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Customer, AdminCustomer)
admin.site.register(product, Adminproduct)
admin.site.register(Category,AdminCategory )