
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import *
from cart.models import *


class SignupForm(UserCreationForm):
	password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'id': 'password1'}))
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"username",
			'id':"username",
			'placeholder':"Choose a username",
			'autocomplete': "username"

			})
		self.fields["email"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"email", 
			'name':"email",
			'id':"email",
			'placeholder':"Email",
			'autocomplete': "email"
			})
		self.fields["password1"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"password1",
			'id':"password1",
			'placeholder':"Password",
			'autocomplete': "password"
			})
		self.fields["password2"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"password2",
			'id':"password2",
			'placeholder':"Confirm Password",
			'autocomplete': "confirm-password"
			})


	class Meta:
		model=User
		fields=('email','username','password1','password2')


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