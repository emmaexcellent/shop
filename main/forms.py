
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import *
from cart.models import *


class SignupForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"username",
			'id':"username",
			'placeholder':"Choose a username"
			})
		self.fields["email"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"email", 
			'name':"email",
			'id':"email",
			'placeholder':"Email"
			})
		self.fields["password1"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"password1",
			'id':"password1",
			'placeholder':"Password"
			})
		self.fields["password2"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"password2",
			'id':"password2",
			'placeholder':"Confirm Password"
			})


	class Meta:
		model=User
		fields=('email','username','password1','password2')

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email already in use.')
		return email

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username already in use.')
		return username	

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get('password1')
		username = cleaned_data.get('password2')
		if password != username:
			self.add_error('Your passwords does not match!.')    


class AddressForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["address"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"address",
			'id':"address",
			'placeholder':"Enter Address",
			'rows': 4,
			})
		self.fields["phone"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"number", 
			'name':"phone",
			'id':"phone",
			'placeholder':"Enter Phone Number"
			})
		self.fields["name"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"name",
			'id':"name",
			'placeholder':"Enter the name of place"
			})

	class Meta:
		model= CustomerAddress
		fields=('address','phone','name')