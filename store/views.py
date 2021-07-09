from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, product
# Create your views here.


def index(request):
    products=product.get_all_products()
    category=Category.get_all_category()
    categoryID=request.GET.get('category')

    if categoryID:
        products=product.get_all_products_by_categoryid(categoryID)
    else:
        products=product.get_all_products()
    data={}

    data['products']=products
    data['category']=category
         
    return render(request, 'index.html',data)