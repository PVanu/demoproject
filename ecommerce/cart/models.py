from django.shortcuts import render
from shop.models import Product
from django.contrib.auth.models import User
class Cart(models.Model):

    product =  models.ForeignKey(Product,on_delete=models.CASCADE)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name

    def subtotal(self):
        return self.quantity*self.product.price


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_date=models.DataTimeField(auto_now_add=True)
    address=models.TextField()
    phone=models.IntegerField()
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=20,default="pending")
    def __str__(self):
        return self.product.name

class Account(models.Model):
    acctnum=models.IntegerField()
    accttype=models.CharField(max_length=20)
    amount=models.IntegerField()
    def __str__(self):
        return str(self.acctnum)

