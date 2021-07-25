from django.shortcuts import render,redirect
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
        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }


        #validation
        error_message=None
        customer=Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        if(not first_name):
            error_message="First Name Required"
        elif len(first_name)<4:
            error_message="First Name must be 4 Char log or more"
        
        elif not last_name:
            error_message='Last Name Required'
        elif len(last_name)<4:
            error_message="Last Name must be 4 Char log or more"
        elif not phone:
            error_message="Phone Number Required"
        elif len(phone)<11:
            error_message="Phone number must be 11 Digit"
        elif not password:
            error_message="password is required"
        elif len(password)<6:
            error_message="Password must be 6 char"
        elif customer.isExits():
            error_message="Email address already register"

        #save
        if not error_message:

        # print(first_name, last_name, phone, email, password)
           
            customer.register()
            return redirect('index')
        
        else:
            data={
                'error': error_message,
                'values':value,
                

            }
            return render(request,'signup.html', data )