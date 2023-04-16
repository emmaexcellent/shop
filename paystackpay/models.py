from django.db import models
from cart.models import *
from vendor.models import *
from .paystack import PayStack

# Create your models here.

PAYMENT_OPTIONS=(('Cash','Cash On Delivery'),('Transfer','Direct Bank Transfer'),('Paystack','Pay Online [Secured]'))       
        
class Payment(models.Model):
    ref = models.CharField(max_length=21, null=True, blank=True)
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, null=True)
    order_note = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    customer = models.CharField(max_length=300, null=True, blank=True)
    address = models.ForeignKey(CustomerAddress,on_delete=models.CASCADE)
    amount= models.CharField(max_length=100)
    discount= models.CharField(max_length = 100, null=True, blank=True)
    payment_option= models.TextField(choices=PAYMENT_OPTIONS, default='Cash')
    date_created = models.DateTimeField(default=now)
    date_expected= models.DateTimeField(default=now, editable=True, null=True)
    verified = models.BooleanField(default=False, null=True)

    

    class Meta:
        verbose_name_plural='Payment'

    def __str__(self):
        return self.amount

    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(15)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        if self.verified == True:
            items = CartOrderItems.objects.filter(order = self.order)
            for i in items:
                wallet = VendorWallet.objects.get(vendor__name = i.vendor)
                wallet.balance = int(wallet.balance) + int(i.total)
                wallet.save()               
                    
        super().save(*args, **kwargs)
        
    def amount_value(self) -> int:
        return self.amount *100 

    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result["amount"] / 100 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

        