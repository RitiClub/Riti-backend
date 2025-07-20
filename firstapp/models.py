from django.db import models

# Create your models here.

    
class Customer (models.Model):
    customer_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    address=models.TextField()
    contact=models.BigIntegerField()

class Category (models.Model):
    category_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.TextField()

class Product (models.Model):
    product_id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.TextField()
    caption=models.TextField()
    price=models.FloatField()
    discount=models.FloatField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)

class Orders (models.Model):
    order_id=models.IntegerField(primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField() 

class OrderItem(models.Model):
    order_id =models.ForeignKey(Orders , related_name="orders",on_delete=models.CASCADE)
    products_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField()
    date=models.DateField(auto_now=True)


    
