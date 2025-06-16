from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    about_cat = models.TextField(max_length=2000)
    
    def __str__(self):
        return self.cat_name
    

class Products(models.Model):
    
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)        #if a Category is deleted, all products linked to that category will also be deleted automatically.
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='img/')
    avilable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.product.name}" 
    