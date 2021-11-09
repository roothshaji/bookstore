from django.db import models
from django.utils.timezone import now

class Customer(models.Model):
    #cust_id=models.IntegerField()
    fname=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)


class StoreAdmin(models.Model):
    #admin_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Category(models.Model):
    #category_id=models.IntegerField()
    category_name=models.CharField(max_length=100)


class CategoryType(models.Model):
    type_name = models.CharField(max_length=100)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)


class Product(models.Model):
    #product_id=models.IntegerField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    type_id=models.ForeignKey(CategoryType,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=500)
    image_url=models.CharField(max_length=3000)
    price=models.FloatField()
    stock=models.IntegerField()


class Bill(models.Model):
    #bill_id=models.IntegerField()
    cust_id = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    total_price = models.FloatField()
    address = models.CharField(max_length=300)
    order_date = models.DateTimeField(default=now, blank=True)
    order_status = models.CharField(max_length=50)


class BillItems(models.Model):
    order_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    item_price = models.FloatField()


class Cart(models.Model):
    #cart_id=models.IntegerField()
    cust_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()





