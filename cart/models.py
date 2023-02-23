from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from product.models import *
from main.manager import *

# Create your models here.


class CouponCode(models.Model):
	code = models.CharField(max_length=200, null=True)
	per_off = models.PositiveIntegerField(blank=True, null=True)
	expiry_date = models.DateTimeField(default=now, editable=True)

	def __str__(self): 
		return self.code

class CustomerAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=200, null=True)
    address=models.TextField()
    phone =models.CharField(max_length=15)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural='address'    

    def __str__(self): 
        return self.name             

# Order
status_choice=(
        ('process','In Process'),
        ('delivered','Delivered'),
    )
class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True, blank=True)
    total_amt=models.FloatField()
    discount= models.IntegerField(default=0, null=True, blank=True)
    delivery= models.IntegerField(default=0, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)
    paid_status=models.BooleanField(default=False)    
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)
    order_dt=models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural='Orders'

    def save(self, *args, **kwargs) -> None: 
        if self.code == None:    
            self.code = secrets.token_urlsafe(5)                 
            super().save(*args, **kwargs) 
        elif self.order_status == 'delivered':
            order_delivered(self)     

        else:
            super().save(*args, **kwargs)    

# OrderItems
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    ref=models.CharField(max_length=150, null=True)
    vendor=models.CharField(max_length=150, null=True)
    image=models.ImageField(upload_to="order/", null=True)
    size=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    qty=models.IntegerField()
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='Order Items'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image))

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Wishlist'		


class Tracking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Ordercode = models.CharField(max_length= 500)

    def __str__(self):
        return self.Ordercode
