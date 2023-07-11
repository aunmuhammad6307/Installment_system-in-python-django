from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name= 'Customer name',max_length=200, null=True)
    father_name = models.CharField(verbose_name= 'Customer father name',max_length=200, null=True)
    cast = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(verbose_name='Address',max_length=200, null=True)
    phone = models.CharField(verbose_name='Phone number',max_length=12)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    photo_of_customer = models.ImageField(upload_to='customer/customer_photo/%Y/%m/%d/', blank = True)
    customer_signature = models.ImageField(upload_to='customer/customer_signature_photo/%Y/%m/%d/', blank = True)

    def __str__(self):
	    return self.name

class Products(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Original_price = models.FloatField(null=True)
    Installment_price = models.FloatField(null=True)
    Monthly_installment = models.FloatField(null=True)
    addvance_price = models.FloatField(null=True)
    
    def __str__(self):
	    return self.name

class Order(models.Model):

    id = models.BigAutoField(primary_key=True)
    order_ID = models.IntegerField(verbose_name= 'Order ID' , unique=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete= CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.customer.name} {self.product.name}'


class Receipt(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete= CASCADE)
    price = models.FloatField(null=True)
    dealer_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class Installment(models.Model):

    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete= CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete= CASCADE)
    STATUS = (
        ('Pending' , 'Pending'),
        ('Promised' , 'Promised'),
        ('Given' , 'Given')
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.customer.name


    