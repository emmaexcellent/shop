from django.db import models
from colorfield.fields import ColorField
from main.models import *
from vendor.models import *
from ckeditor.fields import RichTextField
from django.utils.timezone import now
from django.utils.html import mark_safe
import secrets
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.

stock_status =(
        ('1','In Stock'),
        ('2','Out Of Stock'),
        ('3','Pre-order'),
    )

class Product(models.Model):
        vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE, null=True)
        name=models.CharField(max_length=200)
        thumb_nail = models.ImageField(upload_to="product_img/", null=True, storage=gd_storage)
        short = models.CharField(max_length=100, null=True)
        category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
        sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE, null=True)	
        color = models.CharField(max_length=100, null=True, blank=True)
        brand = models.CharField(max_length=100, null=True, blank=True)
        number=models.PositiveIntegerField(default=1, null=True, blank=True)
        ref=models.CharField(max_length=100, null=True, blank = True)
        description=models.TextField()
        date=models.DateTimeField(default=now)
        new=models.BooleanField(default=False)
        top_deals=models.BooleanField(default=False)
        sales = models.IntegerField(default=0)
        avg_ratings = models.IntegerField(default=0)
        topic_views = models.IntegerField(default=0)

        class Meta:
                verbose_name_plural='Product'

        def __str__(self): 
            return self.name    

        def save(self, *args, **kwargs) -> None: 
            if self.ref == None:       
                self.ref = secrets.token_urlsafe(7) 
                super().save(*args, **kwargs)  
            else:     
                super().save(*args, **kwargs)

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.FileField(upload_to="product_img/", storage=gd_storage)

    class Meta:
        verbose_name_plural='Product Image'

    def __str__(self): 
        return self.product.name #

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))    

SIZE = [
        ("KG", "kilogramme", ),
        ("G", "gramme", ),
        ("XL", "extra-large", ),
    ]

class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    stock_status = models.CharField(choices=stock_status,default='In Stock',max_length=150)
    size_par = models.CharField(choices=SIZE,default='kilogramme',max_length=150, blank=True, null=True)
    size=models.CharField(max_length=100, null=True)
    price=models.PositiveIntegerField(default=0, null=True)
    dis_price=models.PositiveIntegerField(default=0, null=True)
    discount=models.IntegerField(null=True, blank=True)

    class Meta:
    	verbose_name_plural='Variations'

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs) -> None: 
        if self.dis_price == 0:
            super().save(*args, **kwargs)
        else:    
            discount = int(self.price) - int(self.dis_price)
            self.discount = discount * 100/int(self.price)
            super().save(*args, **kwargs) 

class ProductInformation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    manufacturer=models.CharField(max_length=100, null=True)
    ingredients = models.CharField(max_length=300, null=True, blank = True)
    package = models.CharField(max_length=300, null=True, blank=True)
    item_number=models.CharField(max_length=300, null=True, blank=True)
    prod_date=models.DateTimeField(default=now, editable=True)
    expiry_date=models.DateTimeField(default=now, editable=True)

    class Meta:
        verbose_name_plural='Product Info'

    def __str__(self):
        return self.product.name

class ProductCare(models.Model):
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        care = models.CharField(max_length=500, null=True)

        class Meta:
                verbose_name_plural='Product care'

        def __str__(self):
                return self.product.name


RATING=(
    ("1",'1 Star'),
    ("2",'2 Stars'),
    ("3",'3 Stars'),
    ("4",'4 Stars'),
    ("5",'5 Stars'),
)
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)    
    product = models.ForeignKey(Product,on_delete=models.CASCADE)   
    text=models.TextField()
    rating=models.IntegerField(choices=RATING,default=1)
    date=models.DateTimeField(default=now)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.product               