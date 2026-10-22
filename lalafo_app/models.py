from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    category_name= models.CharField(max_length=32, unique=True)
    category_image= models.ImageField(upload_to='Category_image/')

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name= models.CharField(max_length=100)
    product_price= models.PositiveSmallIntegerField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image= models.ImageField(upload_to='product_image/')
    descriptions= models.TextField()
    phone_number= PhoneNumberField()
    city= models.CharField(max_length=32)
    type=models.BooleanField(default=False)
    create_date= models.DateTimeField(auto_now_add=True)
    owner= models.CharField(max_length=32)

def __str__(self):
    return self.product_name


