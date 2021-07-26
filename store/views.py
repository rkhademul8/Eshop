from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category, product, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
# Create your views here.
#password check True or False
# print(make_password('1234'))
# print(check_password('12345','pbkdf2_sha256$260000$tZQEMu9EcZmxCJ549VdBtM$Yh9ySVjZDhYPMfAnYrjVpU2Hqh4sQn/DwOlmlChqPMM='))

class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        print(product)
        return redirect('index')
        

    def get(self,request):
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
        # check session is work or not
        # print('you are:', request.session.get('customer_email',))    
        return render(request, 'index.html',data)

        



   




class Signup(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
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
       
        error_message=self.validationCustomer(customer)


        #save
        if not error_message:

        # print(first_name, last_name, phone, email, password)
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('index')
        
        else:
            data={
                'error': error_message,
                'values':value,
                

            }
            return render(request,'signup.html', data )
     
    def validationCustomer(self,customer):
        error_message=None
        if(not customer.first_name):
                error_message="First Name Required"
        elif len(customer.first_name)<4:
                error_message="First Name must be 4 Char log or more"
            
        elif not customer.last_name:
                error_message='Last Name Required'
        elif len(customer.last_name)<4:
                error_message="Last Name must be 4 Char log or more"
        elif not customer.phone:
                error_message="Phone Number Required"
        elif len(customer.phone)<11:
                error_message="Phone number must be 11 Digit"
        elif not customer.password:
                error_message="password is required"
        elif len(customer.password)<6:
                error_message="Password must be 6 char"
        elif customer.isExits():
                error_message="Email address already register"
        
        return error_message



class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['customer_email']=customer.email
                return redirect('index')
            else:
                error_message="Email pr password invalid!!"

        else:
            error_message="Email or passwprd invalid!!"
        # print(customer)
        # print(email,password)
        return render (request, 'login.html',{'error':error_message})


        