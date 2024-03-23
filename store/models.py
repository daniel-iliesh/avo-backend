from django.db import models

# Create your models here.
class Collection(models.Model):
    title = models.TextField()

class Product(models.Model):
    title = models.TextField()
    description = models.CharField(max_length=200)
    inventory = models.IntegerField()
    price = models.FloatField()
    collection_id = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)

class Customer(models.Model):
    email = models.EmailField()
    password = models.TextField()

class Cart(models.Model):
    created_at = models.DateTimeField()

class CartItem(models.Model):
    quantity = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    placed_at = models.DateTimeField()

class OrderItem(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

