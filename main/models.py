from django.db import models
from django.utils.timezone import now
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

# Create your models here.

class Category(models.Model):
	title=models.CharField(max_length=60)
	image=models.ImageField(upload_to="category", storage=gd_storage)
	svg = models.FileField(upload_to="svg", null = True , blank= True, storage=gd_storage)

	class Meta:
		verbose_name_plural='Categories'

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" height="50" />'%(self.image.url))	

	def get_absolute_url(self):
            return f'/shop/{self.title}-{self.id}'	

	def __str__(self):
		return self.title

class SubCategory(models.Model):
	category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
	svg = models.FileField(upload_to="svg",null = True,blank= True, storage=gd_storage)
	title=models.CharField(max_length=60)

	class Meta:
		verbose_name_plural='Sub Categories'

	def get_absolute_url(self):
		return f'/shop/{self.title}'		

	def __str__(self):
		return self.title

class Faq(models.Model):
	question = models.CharField(max_length=300)
	answer = RichTextField()

	def __str__(self):
		return self.question

class Contact(models.Model):
	email = models.EmailField()
	phone = models.IntegerField()
	message = models.CharField(max_length=500)

	def __str__(self):
		return self.email	

RATING=(
    ("1",'1 Star'),
    ("2",'2 Stars'),
    ("3",'3 Stars'),
    ("4",'4 Stars'),
    ("5",'5 Stars'),
)

class ExcelcartReview(models.Model):
	name=models.CharField(max_length=200)
	job = models.CharField(max_length=100)
	image = models.ImageField(upload_to="testimonials", null=True)
	title = models.CharField(max_length=200)	
	message = models.CharField(max_length=500)
	star =models.CharField(choices=RATING,max_length=150)
	def __str__(self):
		return self.name


class UserToken(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE)
	token = models.CharField(max_length=100)

	def __str__(self):
		return self.user.username


class Country(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural='Countries'

	def __str__(self):
		return self.name

class State(models.Model):
	name = models.CharField(max_length=200)
	country = models.ForeignKey(Country,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=200)
	state = models.ForeignKey(State,on_delete=models.CASCADE, null=True)
	price = models.IntegerField(null=True, blank=True)

	class Meta:
		verbose_name_plural='Cities'

	def __str__(self):
		return self.name		
