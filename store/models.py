from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=200)
    
    def register(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length=20, null=True, blank=True )

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_category():
        return Category.objects.all()


class product(models.Model):
    
    name=models.CharField(max_length=50, null=True, blank=True)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200, default='', null=True, blank=True)
    image=models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_all_products():
        return product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return product.objects.filter(category=category_id)
        else:
            return product.get_all_products()