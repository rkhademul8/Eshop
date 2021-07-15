from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, product, Customer
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


def signup(request):
    if request.method == 'GET':

        return render(request,'signup.html')
    else:
        postData=request.POST
        first_name=postData.get('f_name')
        last_name=postData.get('l_name')
        phone=postData.get('numer')
        email=postData.get('email')
        password=postData.get('password')


        #validation
        error_message=None
        if(not first_name):
            error_message="First Name Required"
        elif len(first_name)<4:
           
            error_message='First Name must be 4 char or more'
        #save
        if not error_message:

        # print(first_name, last_name, phone, email, password)
            customer=Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
            customer.register()
        
        else:
            return render(request,'signup.html', {'error': error_message} )