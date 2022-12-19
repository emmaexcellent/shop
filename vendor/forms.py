from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["name"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_name",
			'id':"prod_name",
			'placeholder':"Product Name"
			})

		self.fields["short"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_short",
			'id':"prod_short",
			'placeholder':"Short Description",
			})
		self.fields["thumb_nail"].widget.attrs.update({
			'required':'',
			'class':"form-control form-choose",
			'type':"file", 
			'name':"prod_thumb",
			'id':"prod_thumb",
			})
		self.fields["category"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_cat",
			'id':"prod_cat",
			'placeholder':"Choose Category",
			})
		self.fields["sub_category"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_sub_cat",
			'id':"prod_sub_cat",
			'placeholder':"Choose Sub-Category",
			})
		self.fields["color"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_color",
			'id':"prod_color",
			'placeholder':"Product Color",
			})
		self.fields["brand"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_brand",
			'id':"prod_brand",
			'placeholder':"Product Brand",
			})
		self.fields["description"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_desc",
			'id':"prod_desc",
			})

	class Meta:
		model= Product
		fields=('name','short','category','sub_category','color','brand','description','thumb_nail')


class VariationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["stock_status"].widget.attrs.update({
			'required':'',
			'class':"s-example-basic-single w-100 form-control",
			'type':"text", 
			'name':"stock_status",
			'id':"stock_status",
			'placeholder':"Status of product",
			})
		self.fields["number"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_number",
			'id':"prod_number",
			'placeholder':"Product Number in Stock"
			})
		self.fields["size"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_size",
			'id':"prod_size",
			'placeholder':"Size of product according to product unit size"
			})
		self.fields["price"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"number", 
			'name':"prod_price",
			'id':"prod_price",
			'placeholder':"Product Original Price"
			})
		self.fields["dis_price"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"number", 
			'name':"prod_discount",
			'id':"prod_discount",
			'placeholder':"Discount Price Of Product"
			})

	class Meta:
		model= Variation
		fields=('stock_status','number','size','price','dis_price')		


class ProductInfoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["manufacturer"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_manu",
			'id':"prod_manu",
			'placeholder':"Product Manufacturer",
			})
		self.fields["ingredients"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_ingr",
			'id':"prod_ingr",
			'placeholder':"Product Ingredients",
			})
		self.fields["item_number"].widget.attrs.update({
			'class':"form-control",
			'type':"text", 
			'name':"prod_ingr",
			'id':"prod_ingr",
			'placeholder':"Number written on Product",
			})
		self.fields["prod_date"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"date", 
			'name':"prod_date",
			'id':"prod_date",
			'placeholder':"Product Manufacturing Date",
			})
		self.fields["expiry_date"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"date", 
			'name':"prod_expiry",
			'id':"prod_expiry",
			'placeholder':"Product Expiry Date",
			})

	class Meta:
		model= ProductInformation
		fields=('manufacturer','ingredients','item_number','prod_date',
			    'expiry_date'
			)		


class VendorForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["name"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"vendorname",
			'id':"vendorname",
			'placeholder':"Vendor Name",
			})
		self.fields["image"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"file", 
			'name':"vendorimage",
			'id':"vendorimage",
			'placeholder':"",
			})
		self.fields["category"].widget.attrs.update({
			'class':"form-control",
			'type':"text", 
			'name':"vendorcat",
			'id':"vendorcat",
			'placeholder':"Product Category",
			})
		self.fields["description"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"vendordesc",
			'id':"vendordesc",
			'placeholder':"Description",
			'cols':"4o",
			'rows': "10"
			})
		self.fields["address"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"vendoradd",
			'id':"vendoradd",
			'placeholder':"Vendor Address",
			})
		self.fields["phone"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"date", 
			'name':"vendorcontact",
			'id':"vendorcontact",
			'placeholder':"Phone Contact",
			})
		self.fields["email"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"email", 
			'name':"vendormaily",
			'id':"vendormail",
			'placeholder':"Vendor Email",
			})

	class Meta:
		model= Vendor
		fields=('name','category','address','email','description','image','phone')		

