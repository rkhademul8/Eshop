from django.db import models

# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=20, null=True, blank=True )

    def __str__(self):
        return self.name


class product(models.Model):
    
    name=models.CharField(max_length=50, null=True, blank=True)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField(max_length=200, default='', null=True, blank=True)
    image=models.ImageField(upload_to='upload/products/')

    @staticmethod
    def get_all_products():
        return product.objects.all()