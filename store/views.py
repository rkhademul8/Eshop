from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.


def index(request):
    prds=product.get_all_products()
    return render(request, 'index.html',{'products':prds})