
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import *


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
